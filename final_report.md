# Linguistic Markers of Catalan Substitution
Jana Bruses | janabruses@pitt.edu | University of Pittsburgh | Apr 29th

## 0. Introduction
Language endangerment is usually noticed when it's too late and it’s past the point of no return. Fortunately, we are aware of Catalan's endangerment, which is still classified at the lowest threat level in the UNESCO danger list. This project wants to use this rare opportunity to explore the specific position of Catalan's threat, which lies in its Spanish substitution, with the goal of finding traces or markers in the changes of the language itself. Most of the evidence of Catalan's substitution is found in society and societal behaviors, but this project aims to find the evidence in linguistic features, looking for variation and changes through time that mark and help evaluate language substitution.

## 1. Background
Catalan's endangerment tipping point is the Francoist Dictatorship from 1939 to 1975. Before the Dictatorship, Catalan was the habitual language in Catalonia in any domain. However, after Spanish was imposed and Catalan was limited to private environments, it has been in a subordinate position. This year, only 1/3 of the population reported it as their habitual language, as we keep shifting from Catalan to Spanish in our daily lives. Socially, the danger is clear. Looking at language only, how can we diagnose this substitution?

While there is the misconception that word incorporations are the most remarkable marker of language substitution, Catalan's history has proved otherwise. The Francoist Dictatorship, with Catalan's ban and persecution in any public space and Spanish being imposed in the media, schools, workplaces, etc, led to many word incorporations in Catalan spoken in private. However, after the dictatorship, the word incorporations were progressively substituted by their Catalan versions for the most part, so this is not a definitive change, and can be reversed. What Dr. Junyent, a leading advocate for Catalan’s preservation, suggests as real symptoms of endangerment that are language-threatening losses are:
1. Loss of word classes absent in the dominant language.
2. Time and space lexicon modification.
3. Syntactic restructuring.

In this project, we look at specific pieces of Catalan representative of each of these areas of potential loss. The specifics can be found in the Analysis. [Analysis-1-LowLevel](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/Analysis-1-LowLevel.ipynb)|[nbviewer](https://nbviewer.org/github/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/Analysis-1-LowLevel.ipynb)

## 2. Data
### 2.1 Overview
To look for linguistic variation and changes through time, spoken data would have been the best data resource. However, aiming for a long enough time span wasn't a possibility, as older spoken records are far more challenging to find than written records. Still, as written language always shows linguistic phenomena later than spoken language, the data I decided to settle for were written records derived from spoken works, meaning speeches, parliament sessions, and such.

Specifically, the data used in this project consisted of:

| Corpus                         | Years             |  Notes             |
|------------------------------------|-------------------|-------------------|
| **CTIC**                    | 1832–1926            | 28 Ceremonial speeches 	            |
| **Parlament Parla**                    | 2007–2018          | 700 hours total Parliament sessions    |
| **ParlaMint-ES-CT**                 | 2015–2022            | Multilingual/Comparable Parliament corpus  |
| **Radioteca.cat**   | 1985-2025 | Library of AI transcribed Radio broadcasts |

Initially, Radioteca.cat was not included in our data as it is less genre-specific. That is, Radioteca.cat is more informal than any of the other sources of data we have. However, using only the first three dataframes gave us a gap from 1926 to 2007. Therefore, Radioteca.cat was brought in.

### 2.2 Adquistion and Parsing
The whole process is done in [Data-Parsing-Exploratory-Analysis-2](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/Data-Parsing-Exploratory-Analysis-2.ipynb)|[nbviewer](https://nbviewer.org/github/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/Data-Parsing-Exploratory-Analysis-2.ipynb)\
Briefly, the acquisition and parsing were:

For CTIC, it was downloaded as separate text files with metadata mixed in. Therefore, it was parsed using Beautiful Soup. The metadata and text pieces were stored in a pandas dataframe.
For Parlament Parla, it was a folder of .tsv files, therefore the data was simply turned into a pandas dataframe.
For ParlaMint-ES-CT, it contained files in many formats. TSV documents were used to acquire the metadata and TXT files for the text content/transcription. Both were loaded into a single pandas dataframe. 
For Radioteca.cat, since it's a web library, it was webscraped using Beautiful Soup and a CSV file containing the metadata provided by the owner of the Radioteca project. For the data currently used for the analysis, only shows broadcast before 2012 were taken, as we already had lots of data for the recent years. However, as some gaps were found in the data during the analysis, such as a gap in 2019, Radioteca.cat was re-scraped completely, the whole library this time, which can be found in: [Data-Parsing-Exploratory-Analysis-Part1.ipynb](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/Data-Parsing-Exploratory-Analysis-Part1.ipynb) | [nbviewer](https://nbviewer.org/github/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/Data-Parsing-Exploratory-Analysis-Part1.ipynb) and its continuation [CompleteDataFrame.ipynb](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/CompleteDataFrame.ipynb) | [nbviewer](https://nbviewer.org/github/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/CompleteDataFrame.ipynb), which is still in progress. Due to the time constraint, I wasn't able to perform the analysis on the new data. Therefore, the term project analysis and conclusions are using the data from CTIC, Parlament Parla, ParlaMint-ES-CT, and Radioteca.cat up until 2012.
After acquiring the separate corpora and storing them in dataframes, a single pandas dataframe was created, merging all of them. The texts were also tokenized after the merging using Pitt's supercomputing. The files can be found in under "tokenization.*".
After the acquisition and data parsing, the resulting dataframe was very unbalanced. To reduce the imbalance while avoiding biases, individual speaker contributions were limited to 1500 characters, and for Radioteca, episode contributions were also limited to 1500 characters, ensuring a less topic- and speaker-specific dataframe.

The resulting dataframe used for the analysis consists of **3 billion tokens** from **75 thousand text-pieces** which are single speaker contributions. 

## 3. Analysis
The analysis was performed based on Dr. Junyent's language threatening symptoms mentioned previously. For each of the risk areas, specific elements of Catalan were chosen to be evaluated. These are:
1. For Loss of Word Classes: Pronouns. Specifically, the unstressed pronoun "hi".
2. For Time and Space Lexicon Modification:
   1. The directional verbs "anar" and "venir"
   2. The perifrastic past and simple past
3. For Syntactic Restructuring:
   1. Tenir que vs haver de
   2. Pronominalized Verbs

Most of the analysis was based on counts per year. Since the raw counts were not very valuable, as the data size per year is very uneven, the counts were always turned into a percentage of the total number of tokens for that text. That is, all of the results are like a "proportion" of the tokens that match our target in that text.

Link to analysis section: [Analysis-1-LowLevel.ipynb](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/Analysis-1-LowLevel.ipynb)|[nbviewer](https://nbviewer.org/github/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/Analysis-1-LowLevel.ipynb)

### 3.1 Unstressed Pronoun Hi
**Context:** Neutral unstressed pronouns don't exist in Spanish. In Catalan, we have "en" and "hi". Since "hi" does not have any other function than as an unstressed pronoun, it was easier to work with it than "en".
**Hypothesis:** Since Spanish does not have the neutral unstressed pronoun word class, the frequency of the use of "hi" might be decreasing, and we might be losing that word class.\ 
**Method:** I looked for "hi" in the token lists using regex. Once found, I stored them in a list and got the count of found "hi" that was turned into a percentage out of the tokens of the text. The percentages were averaged per year to have a yearly percentage of "hi".
**Results:** There was no significant change in the use of "hi" in our data. Its use doesn't present any trends.

### 3.2.1 Directional verbs "anar" and "venir"
**Context:** Catalan has a clear distinction between motion towards and away from the speaker with "anar" - "to go" and "venir" - "to come". In Spanish, while the distinction exists it is less strict.\
**Hypothesis:** Since in Spanish the distinction between motion away from and toward the speaker in verbs is less strict, the distinction might be getting blurred with one of the two verbs expanding its use into contexts formerly reserved for the other.\ 
**Method:** The text was lemmatized so we could find any form of the verbs with their infinitive form. Then, the verbs were found in the lemmatized text and stored in two separate lists in two separate columns. The count for them was calculated and added across the texts belonging to the same yeare and then turned into a percentage out of the total tokens for that year. 
**Results:** There is a significant change in the use of "anar" which has been increasing over time. However, that has not affected the use of "venir" which is stable all throughout our data. These results support an extension of the verb "anar", whose use has been broadened. However, unlike what we predicted, this has not affected "venir".

### 3.2.2 Perifrastic Past
**Context:** Perifrastic past in Catalan is a verb tense used to express past tense actions that were done in the past and have been finished. It is formed with "anar" in the past tense as the auxiliary plus the main verb in its infinitive form. It is equivalent to Past Simple, which we also have in Catalan.\
**Hypothesis:** Since in Spanish perifrastic past does not exist, its use might be dropping as we can use other past tenses in its place.\
**Method:** Using the lemmatized text verbs forms matching the pattern for Perifrastic Past were found using regex. Then they were counted and turned into a percentage being the proportion of Perifrastic Past instances out of the total tokens in that dataframe.
**Results:** There is no significant change in the use of Perifrastic Past. No tendencies can be found in its use throughout the years.

### 3.2.1 Haver de VS Tenir que
**Context:** In Catalan the periphrase "Haver de" is used for tasks and obligations. In Spanish the periphrase for that context is "Tener que", which would be literally translated to Catalan as "Tenir que", as "tenir" is "tener", both meaning "to have".
**Hypothesis:** Since in Catalan we have a literal translation of "Tener que" from Spanish, we might be using "Tenir que" as a literal translation instead of "Haver de".\
**Method:** Turned the lemmatized text into a bigram list where I looked for matching "haver de" and "tenir que". I stored them in separate lists in separate columns. Then counted them per year and turned them into the proportion out of the total tokens for that year so they could be compared.
**Results:** There is no significant change in the use of "Haver de" and no increase in the use of the literal translation "Tenir que", which is barely found in our data.

### 3.3.2 Pronominalized Verbs
**Context:** Both Catalan and Spanish have pronominalized verbs, where the verb requires a pronoun. In Spanish, movement verbs are pronominalized, while in Catalan they are not.\
**Hypothesis:** Verb pronominalization might be increasing due to Spanish influence, as we might be pronominalizing verbs that used to not be pronominal.\
**Method:** Created a (POS tag, word) tuple list, then looked for verbs and clitics preceding and following them, as in Catalan, pronouns working with pronominal verbs are clitics.
**Results:** There is no significant change in verb pronominalization through time. 
![png](image_files/output_8_0.png)

## 4. Conclusion
This project aimed to find traces of Catalan's substitution in language by looking at different elements of the language that could point to and help us analyze and quantify its substitution. Out of the five different features of Catalan at the different levels of language explored in the project, one of them showed some significant results, even though it did not allow us to see traces of substitution. The analysis on Time and Space Lexicon modification uncovered a meaning extension for the directional verb "anar." Still, no substitution was observed, as it did not substitute "venir", whose use stayed consistent throughout the years. No relevant variation or changes were found that mark Loss of Word Classes or Syntactic Restructuring through the specific pieces analyzed.

# 5. Further
While none of the analysis portions allowed us to see substitution happen through time, I believe that the imbalanced data and the different genres of text did not help us get the results we were aiming for. In view of that, I'm considering using only the full Radioteca as a data source, as it is a very extensive resource and has a very specific genre and style. Moreover, it is a direct transcription of radio broadcasts, which is closer to spoken daily language than a prepared ceremonial speech or a discussion at the parliament, which are rehearsed, prepared, and formalized.
Also, after the first analysis, a second part was done, training 3 models. Two Naive Bayes classifiers on tf-idf features were trained, which allowed us to classify the texts belonging to different time periods, and can be found in [Analysis-2-TextLevel.ipynb](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/Analysis-2-TextLevel.ipynb) | [nbviewer](https://nbviewer.org/github/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/Analysis-2-TextLevel.ipynb). A Random Forest model was also trained using the percentages of our chosen and analyzed features, but it did not have a very good accuracy, which matches our mostly insignificant results.

## 5. Challenges and Setbacks
The biggest challenge working with this project was trying to get the data to be more balanced. I tried different methods to reduce the amount of data in the most recent years, still, it wasn't effective enough. Working with this big amount of data was also problematic, as tokenization and any step requiring Stanza had to be done using Supercomputing. However, both challenges are natural considering we wanted to analyze variation through time, which required a big amount of data and old data that is not easily found.

## 6. References
- Carme Junyent. (2023,  9). El català és una llengua en procés d’extinció. La Directa. 
[https://directa.cat/el-catala-es-una-llengua-en-proces-dextincio/](https://directa.cat/el-catala-es-una-llengua-en-proces-dextincio/)
- Montoya Abat, B., & Mas i Miralles, A. (2013). La variació lingüística a la Governació d’Oriola. Treballs de sociolingüística catalana, (23), 103–115. [https://raco.cat/index.php/TreballsSocioling/article/view/281158]
- 3Cat. (2022, 15 de juny). El futur del català a "Sense ficció": el català, en perill d'extinció?. [https://www.3cat.cat/3cat/el-futur-del-catala/noticia/3160173/]