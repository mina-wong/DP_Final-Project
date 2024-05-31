# DP_Final-Project

## Project Description

### Research Question
How has innovation changed between 2017-2023 in various countries?

Additionally, which region had the highest innovation overall? Which region has the highest score in each component? Was there any effect on innovation in these regions after Covid-19? 

### Overview
This project aims to analyze patent data and extract useful datapoints to build an innovation index. It will additionally make interactive plots to understand and compare the development of innovation for different countries between 2000 and 2023.

Countries selected: 
 - Ecuador (EC)
 - Uruguay (UY)
 - Vietnam (VN)
 - Belarus (BY)
 - Monaco (MC)

### Data Collection

The index itself is referenced from a study conducted by Ponta, Puliga and Manzini. It uses patent data to calculate scores for 5 components intended to measure different aspects 

    Citation: 
    Ponta, L., Puliga, G. and Manzini, R. (2021), "A measure of innovation performance: the Innovation Patent Index", Management Decision, Vol. 59 No. 13, pp. 73-98. https://doi.org/10.1108/MD-05-2020-0545

Patent data was extracted from [Espacenet](https://worldwide.espacenet.com/), an online patent search service developed by the European Patent Office. Some data was taken from the [World Bank](https://data.worldbank.org/indicator/SL.TLF.TOTL.IN) to calculate the final indicators. 

Countries with relatively relatively smaller sized datasets were selected for this project. The code can be run for different regions for further analysis.


## Code files
This project includes three code files: `importData.ipynb`, `dataProcessing.ipynb`, and `visualiseData.ipynb`. Output is saved in subfolder `/data`. Region specific files and projects are placed within folders named as their respective country code (e.g. `PatentsProject/data/NL`).

### 1. importData.ipynb

This file extracts raw patent data from Espacenet. Variables "startYear", "endYear", and "regionCode" can be adjusted as necessary. Returns pickle file holding a list of patent data in `/data/REGION` folder.


### 2. dataProcessing.ipynb

Takes raw data from json files and extracts family Number, application number & date, publication number & date, patent name & abstract, applicant & inventor name, IPC & CPC classes, family members, number of geographical extensions, and oldest and newest family publication. Processed data is returned in a CSV file `/data/NL/1990-23NLPatents.csv`. File names and location will be adjusted accordingly. 

It then referenecs Espacenet and Google Patents to extract the number of backward and forward citations for each patent. Returns a csv file named `/data/NL/1990-23NLPatentsWithCitations.csv`.

### 3. visualiseData.ipynb

Takes cleaned patent data and uses it to calculate IPI indicators. World Bank labour force statistics are referenced. 

Takes the calculated IPI indicators and creates 3 visuals:
    1. Multiple line graph to track changes in overall IPI over time in the 5 regions
    2. Stacked bar graph to visualise changes in overall IPI and its components given a certain year. Includes an out-of-notebook extension with interactive year selection feature. 
    3. Radar graph for clearer comparison of the components of the index. Includes interactive widgets to select which region and year is being displayed. Also includes a zoom bar to scroll in and out of the graph