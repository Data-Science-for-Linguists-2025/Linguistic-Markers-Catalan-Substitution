import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import re
import glob
from requests.exceptions import RequestException

radioteca_df = pd.read_csv("TranscripcionsRadioteca.csv", header = 0)
radioteca_df.columns = ["Date", "Publisher", "Program_name", "Title", "URL"]
radioteca_df.head()
radioteca_df["Date"] = pd.to_datetime(radioteca_df["Date"])
radioteca_df["Year"] = radioteca_df["Date"].dt.year
item =(radioteca_df[pd.isnull(radioteca_df["Date"]) == True]).index
print(item)
radioteca_df = radioteca_df.drop(item)  # it's just one row NaN so we'll just drop that one

# setting the URL as index so we can scrape the pages more easly
radioteca_df = radioteca_df.set_index("URL")

# global session object to be reused for much faster scraping
session = requests.Session()

def scrape_radiotecafile(file):
    '''
    Function to scrape Radioteca.cat
    makes a GET request to retrieve the webpage content 
    
    Scaping section: 
    "transcript-container" - contains transcript
    if container exists we iterate through "transcript-segment(s)" within
    and extract: 
    1- line id - as "transcript-speaker" (format: SpeakerTimestamp)
    2- speaker - the first 5 characters of the line-id
    3- time - "transcript-time"
    4- text/line - "transcript-text"

    to this data then we add:
    the date, the publisher, the program name, the title and the year
    all from the radioteca dataframe we created after the csv file previously

    all data is attached to the content dictionary as a list, where the key is the line_id
    the dictionary is returned
    '''

    # request
    response = session.get(url)  
    response.raise_for_status()

    # fetch
    soup = BeautifulSoup(response.text, "html.parser")
    transcript_section = soup.find("div", class_="transcript-container")
    content = {}


    if transcript_section:
        for segment in transcript_section.find_all("div", class_="transcript-segment"):
            # get the text of the transcipt
            segment_text = segment.get_text(strip=True)
            
            # extracting the line_id (speaker+time), speaker, time and the text
            if segment.find("p", class_="transcript-text"):
                line_id = segment.find("div", class_="transcript-speaker").get_text(strip=True)
                speaker = line_id[:5]
                time = segment.find("span", class_="transcript-time").get_text(strip=True)
                text = segment.find("p", class_="transcript-text").get_text(strip=True)

                # getting metadata from the dataframe resulting from the csv
                metadata = radioteca_df.loc[url]
                content[line_id] = [speaker, time, text, metadata["Date"], metadata["Publisher"], 
                                    metadata["Program_name"], metadata["Title"], url, metadata["Year"]]
                
    return content


if __name__ == "__main__":
    from tqdm import tqdm

    radioteca_lines_list = []

    for url in tqdm(radioteca_df.index):
        if pd.isna(url) or not (url.startswith("http://") or url.startswith("https://")):
            continue
        
        try:
            dictionary = scrape_radiotecafile(url)
        except RequestException as e:
            continue

        if dictionary is None:
            continue
            
        try:
            for key, value in dictionary.items():
                row = {
                    "Line_id": key,
                    "Speaker": value[0],
                    "Time": value[1],
                    "Text": value[2],
                    "Date": value[3],
                    "Station": value[4],
                    "Show": value[5],
                    "Episode": value[6],
                    "URL": value[7],
                    "Year": value[8]
                }
                radioteca_lines_list.append(row)

        except IndexError:
            print(f"Skipping {key}")
        except Exception:
            print(f"Skipping {key}")

    radioteca_lines_df = pd.DataFrame(radioteca_lines_list)
    radioteca_lines_df.to_pickle("radioteca_df.pkl")

