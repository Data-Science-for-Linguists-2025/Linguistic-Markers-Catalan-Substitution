# Progress Report
Jana Bruses | janabruses@pitt.edu | February 12th 2025

### Report 0 - Project creation
02/12/2025\
Created repository with README.md, LICENCE.md, progress_report.md, project_plan.md and .gitignore.\
Next goals: explore data sets

### Progress Report 1 - Data Processing and Exploratory Analysis
02/26/2025\
**Current stage:** Data parsing & exploratory analysis\
**Next step in current stage:** Adding, parsing and re-exploring data to bridge the gaps found in the actual corpora\
**Next stage:** Data preprocessing 2 (data cleaning and transformation)

#### Progress
I first examined the structure and formats of the target datasets, identifying the tools for parsing and making sure there were no format or line terminator inconsistencies. I ended up working with Pandas for this task.\
I then loaded and explored the dataset, analyzing its structure, inconsistencies and making it more fit for the research purposes. I created a Jupyter Notebook named Data-Parsing-Exploratory-Analysis.ipynb to document the steps taken, including initial parsing, data structuring and analysis to discover inconsitencies with the corpora before diving into the datasets to find traces of Catalan's substitution.\
As part of the exploratory analysis to find any issues before working with the data, I performed surface-level data cleaning, such as removing the title from the text's content, calculated summary statistics for each of the corpora individually and as a whole, and visualized key distributions mostly focusing on timespan coverage. This helped in understanding the overall quality and usability of the dataset for the next stage of processing.

See: [Sample data repo](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/tree/main/data_samples) for data samples\
See: [Data-Parsing-Exploratory-Analysis](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/Data-Parsing-Exploratory-Analysis.ipynb) for a close look at the data processing and analysis of the corpora

#### Next Steps:
**A soon as possible:**
1) Get data to bridge the gap between the CLTIC corpora and the ParlaMint and Parla Parlament Corpora, that is, Catalan data between 1900-2010. Possibly radioteca's transcription of radio program through web scrapping, and parsing with Beautiful Soup. Otherwise, I need to find another corpora or be mindful of that gap during my exploration.
2) Download, load and include the other_clean data from the Parlament Parla corpora. Hasn't been possible due to space issues preventing me to download it and work on it.
3) Perform more in-depth data cleaning.

**Next steps after data adquisition, organization and exploration:**
* Apply transformations needed for further analysis.
* Prepare the dataset for model training and statistical examination.

#### Data Sharing plan:
Since data comes from various resources I will be required to follow the license of the most restrictive one.\
For the CLTIC corpora the files published before 1985 are open for unrestricted free download individually as a single file.\
For the Parlament Parla and ParlaMint corpora, they were published under Creative Commons Attribution 4.0 International that allows for re-distribution and re-use of a licensed work on the condition that the creator is appropriately credited.\
Accordingly, my data will be shared under Creative Commons Attribution 4.0 International, unless I bridge the time gap and data-amount difference in my current data by using a corpora that has a more restrictive license. Then, I would have to change this plan. 

### Progress Report 2 - Wraping up and adjusting the data
03/23/2025\
**Current stage:** Final data adquisition steps, exploratory analysis and adjusting data to our purposes.\
**Next step in current stage:** Tokenizing, which I didn't think about before but probably will be helpful later.\
**Next stage:** Diving into the analysis of the data

#### Progress
The first progress report and the conclusions during the exploratory analysis highlighted some issues with the data. The main goal I worked towards, documented in this second progress report, was to solve those issues.

The **first problem** was a very evident time gap in the corpora. We had no data for the years around the change of century. A fourth resource was found and brought in to patch this gap after receiving permission from the owner, as this is a personal project. The data is "radioteca.cat", a web library of radio emissions in Catalan, summarized and transcribed through AI, later human-revised. The content was web-scraped using Beautiful Soup. The resulting data frame went through Exploratory Data Analysis as with the other three corpora. 

The **second issue**, further emphasized with the addition of this last resource, was the heavily unbalanced distribution of our data. Three strategies were pursued with the goal of keeping the most representative and unbiased part of the data while reducing its amount. **(1)** First, a limit of 1500 characters per individual contributor was set avoiding too much speaker-specific information. **(2)** Secondly, for Radioteca, a limit of 1500 characters per episode was set, aiming for less topic-specific data. **(3)** Lastly, the previous approach of setting all parliament-parla's dates as the average date for the corpora, since no specific metadata was provided, was also contributing to an unnatural imbalance. Hence, the dates were reorganized through randomization in the range. 

After the changes, the merged dataset was rebuilt, and the exploratory data analysis was re-done to check how these changes had reshaped our data and see if it now suits our needs and is ready to be worked on.

All these changes and progress were made in the copy of the original Jupyter Notebook for Data Parsing and Exploratory Analysis, named Data Parsing and Exploratory Analysis 2.\
See: [Data-Parsing-Exploratory-Analysis-2](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/Data-Parsing-Exploratory-Analysis-2.ipynb) for a close look at it.\
See: [Sample data repo](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/tree/main/data_samples) for data samples

#### Data Sharing plan:
The owner of Radioteca, the new data brought in after the first progress report, Xavier Drudis, who I contacted to ask for permission and any sharing preferences, allowed me to share data as I found suited. Consequently, we can maintain the sharing plan presented in the previous progress report. That is to follow the license of the most restrictive data resource used, which are the Parlament Parla and ParlaMint corpora with a Creative Commons Attribution 4.0 International license that allows for re-distribution and re-use of a licensed work on the condition that the creator is appropriately credited.\
It also needs to be noted that the CTILC corpora are open for unrestricted free download but only individually as single files; therefore, I will only be sharing a single file as a sample of each corpus. All of them will be cited and linked to their download page.\
The separate resources' data frames and the main data frame have been picked and stored. However, because of the different restrictions, the joined data frame will not be made available.\
Since Parliament Parla's and ParlaMint's data frames are very close to the original data, I believe downloading them from the owners' pages is the best if you want to work with them. [ParlaMint](clarin-eric.github.io/ParlaMint/) [ParlamentParla](https://doi.org/10.5281/zenodo.5541827)\
As mentioned previously, CTILC only allows individual file downloads; hence, to respect the integrity of that data, refer to [CTILC](https://ctilc.iec.cat/scripts/CTILCCorpus_Descarr.asp) to download it.\
For the Radioteca data frame, since the web-scraping process took a long time and the data can't be found anywhere else or in any other than web format, it might be worth sharing for other projects' use. However, I'm still awaiting the owner's confirmation and reviewing any radio shows and transcription licensing issues. If possible, the data frame for Radioteca will be made available with citations to the original Radioteca web page and this project. 

#### License:
I'm still very uncertain about the License because of what was mentioned previously. I want to share the Radioteca data frame in terms of data for reuse. That is limiting my license plan progress. Except for the data portion, the License can be found in: [License.md](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/LICENSE.md) I decided to go with this simple and permissive License because I build on other people's code many times, I don't think I could learn as much without it as a resource, so I hope to allow others to do the same off of mine.

### Progress Report 3 - Headway into the analysis
04/06/2025\
**Current stage:** Starting with low level analysis (3/8 points explored).\
**Next step in current stage:** Finishing low level analysis (7/8) and starting text level analysis. (8/8).

#### Progress
To wrap-up my data I used Stanford's Stanza to tokenize all of the files. This final step of the "data" section is reported and completed in [Data-Parsing-Exploratory-Analysis-2](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/Data-Parsing-Exploratory-Analysis-2.ipynb). However, the tokenization itself was done using Pitt's supercomuputing through command line, for a more efficient processing. The files used for the tokenization (slurm and python script) can be found in the newly created [scripts folder](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/tree/main/scripts) in their respective format.

I started the analysis which will be divided in two levels and done separately in two notebooks: 
1. [Analysis 1 Low Level](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/Analysis-1-LowLevel.ipynb)
2. [Analysis 2 Text Level](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/Analysis-2-TextLevel.ipynb)

The second analysis notebook is just a placeholder at the moment. The analysis work so far has been done at the low level in Analysis 1.\
For the analysis, the points I wanted to explore as presented in the project plan where: (1) Loss of Word Classes, (2) Time and Space Lexicon Modification, (3) Syntactic Restructuring and then as number (4) doing a Text-Level Analysis using Machine Learning. (You can refer to the initial ideas on [project plan](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/project_plan.md)).\
Before diving into them in the analysis 1 notebook I did a brief recap analysis of the data to re-fresh what I'm working with.\
For the analysis sections, each of the exploration lines starts with a brief background on that specific feature of Catalan, and some key points that will help us do the analysis. Then I dive into the analysis itself, although in some situations it required adding some layers to our dataframe, as for example Lemmatization for point 2.1 which was also run on Pitt's supercomputing. The files can be found on the notebook and separately in the [scripts folder](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/tree/main/scripts).\ After the analysis, there's a few lines of conclusion that still have to be revised and improved. At the end of the whole notebook there will be a general overall conclusion.\
So far I've started the exploration with:\
(1) Loss of Word Classes through the frequency of the Pronom Feble "Hi", using the tokenization column. Does not seem to be significant in any way.\
(2) Time and space lexicon modification through:\
    (2.1) Anar and Venir directional distinction frequency analysis. After using lemmatization and comparing the use of anar and venir it seems like      there is a clear tendency that might be indicating a meaning shift. However, it is not necessarly showing one verb's replacement by the other.\
    (2.2) Time lexicon modification through Frequency Analysis of Passat Perifràstic, using the tokenization column again. Shows no clear patterns.

The next analysis efforts will be on:\
Wraping up the conclusions of the previous analysis outcomes'.\
(2.3) Pronominalization of movement verbs still for time and space lexicon modification analysis\
(3) Syntactic restructuring through:\
    (3.1) Tenir que vs haver de
    (3.2) Deletion of subject pronouns\
    (3.3) Deletion of "en" in partitive expressions\
(4)  Text-level analysis

No additions have been made to the data folder, and the license stands the same. 