# Linguistic-Markers-Catalan-Substitution
Jana Bruses | janabruses@pitt.edu | University of Pittsburgh | Apr 29th

Welcome to my term project for Data Science for Linguists!\
Linguistic Markers of Catalan Substitution is an analysis aimed at finding linguistic traces of Catalan's endangerment due to language substitution. 
This project examines morphological, syntactic, lexical, semantic, and text-level changes, looking for empirical evidence in language that Catalan is undergoing a substitution process. Its goal is to detect some symptoms that allow us to quantify and evaluate the substitution process, allowing us to understand more about language endangerment in a rare situation where we are aware of Catalan's endangerment when it is still at the lowest level of endangerment according to UNESCO.  

As the analysis is looking at changes through time it required data that span a long enough time period. A single corpora was unavailable, so four separate corpora were used:\
[CTILC](https://ctilc.iec.cat/scripts/CTILCCorpus_Descarr.asp)
[ParlaMint](clarin-eric.github.io/ParlaMint/)\
[ParlamentParla](https://doi.org/10.5281/zenodo.5541827)\
[Radioteca.cat](https://radioteca.cat/)\
The resulting data consists of about three billion tokens from seventy-five thousand text pieces (meaning individual speaker contributions.) The data spans from 1860 to 2022. However, we have a lot more data from recent years, so the average year for the contributions is about 2008.\
This information is subject to change due to some issues found during the analysis. However, since the analysis portion hasn't been re-done with the newly acquired, parsed, and explored data frame, for now, the data used is what was stated before. 

## Directory:
- **[final_report.md](final_report.md)**: **TO DO** Concluding report of the project for term submission
- [README.md](README.md): the readme file for this project

The following files have been listed in chronological order, they follow the timeline of the project work:
- [project_plan.md](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/project_plan.md): Starting Point of the project. Original plan at the start of the semester.
- [progress_report.md](progress_report.md): Progress reports 0 to 3 on the development and progression of the project
- **Data:** 
    - Data-Parsing-Exploratory-Analysis-2.ipynb [github](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/Data-Parsing-Exploratory-Analysis-2.ipynb) | [nbviewer](https://nbviewer.org/github/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/Data-Parsing-Exploratory-Analysis-2.ipynb): Adquisition, parsing and exploration of the 4 data sets separately followed by the complete dataset and it's analysis.
    - Data-Parsing-Exploratory-Analysis-Part1 [github](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/Data-Parsing-Exploratory-Analysis-Part1.ipynb) | [nbviewer](https://nbviewer.org/github/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/Data-Parsing-Exploratory-Analysis-Part1.ipynb): Adquistion, parsing and exploration of the 4 data sets separately including the complete radioteca up to 2025
    - Complete-Data-Frame.ipynb [github](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/CompleteDataFrame.ipynb) | [nbviewer](https://nbviewer.org/github/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/CompleteDataFrame.ipynb): Reduction, merge and analysis of the complete dataframe with the coplete radioteca included.
- **Analysis:** 
    - Analysis-1-LowLevel.ipynb [github](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/Analysis-1-LowLevel.ipynb) | [nbviewer](https://nbviewer.org/github/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/Analysis-1-LowLevel.ipynb): Lexical, Morphological and Syntactic analysis. 
    - Analysis-2-TextLevel.ipynb [github](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/Analysis-2-TextLevel.ipynb) | [nbviewer](https://nbviewer.org/github/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/Analysis-2-TextLevel.ipynb): Machine learning focused analysis of the data using tf-idf features and our features.
- [data_samples](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/tree/main/data_samples): folder containing a sample data file for each of the corpora
- [images](POSARLINK): **TO DO**
- [scripts](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/tree/main/scripts): folder containing python (.py) and slurm (.sh) files used for processing the data using Pitt's CRC
- [Linguistic-Markers-of-Substitution_Presentation.pdf](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/blob/main/Linguistic-Markers-of-Substitution_Presentation.pdf): slides for the presentation of the project
- [LICENSE.md](LICENSE.md): MIT License for the Project
- [obsolete_files](https://github.com/Data-Science-for-Linguists-2025/Linguistic-Markers-Catalan-Substitution/tree/main/obsolete_files): Folder containing notebooks that are no longer in the project progress line

## Guestbook: 
- [Guestbook](https://github.com/Data-Science-for-Linguists-2025/Class-Lounge/blob/main/guestbooks/jana.md)
