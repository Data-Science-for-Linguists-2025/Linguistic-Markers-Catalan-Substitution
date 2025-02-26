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