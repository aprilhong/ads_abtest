# <p align="center"> :tv: Ads Marketing A/B testing :bar_chart:
  
# Business Case:
**Problem:** The marketing landscape is dynamic, and success depends on finding the most impactful messaging and creatives. Traditional methods often rely on guesswork or past experiences, leading to suboptimal campaign performance and wasted resources. 

The companies are interested in answering two questions:
1. Would the campaign be successful?
2. If the campaign was successful, how much of that success could be attributed to the ads?

**Solution**
A/B testing offers a data-driven approach to campaign optimization. It allows for the simultaneous testing of different campaign variations (web page elements, banners, etc.) with different audience segments. This allows us to identify which version resonates best and drives the most significant impact on key business metrics.

**Methodology**:

1. Exploratory Data Analysis to determine if the campaign is successful.
2. Conduct A/B using Chi-square test of independence
3. Results
4. Conclusion 

**Recommendations**: 


**Conclusion**: 

### Table of Content
<details><summary>Expand/Collapse</summary>

1. [File Descriptions](#file-descriptions)
2. [Technologies Used](#technologies-used)
3. [Executive Summary](#executive-summary)
    1. [Exploratory Data Analysis](#exploratory-data-analysis)
       - [Data Cleaning](#data-cleaning)
       - [Variable Analysis and Visualization](#variable-analysis-and-visualization)
    2. [AB Testing](#ab-testing)
    3. [Results](#results)
    4. [Reccomendations](#recommendations)
    5. 
   
</details>

### File Descriptions

<details><summary>Expand/Collapse</summary>
  
  - [data](https://github.com/aprilhong/ads_abtest/tree/main/data) : folder containing all data files
  - **marketing_AB.csv**: raw dataset from [Kaggle](https://www.kaggle.com/datasets/faviovaz/marketing-ab-testing)
  - [ads.ipynb](https://github.com/aprilhong/ads_abtest/blob/main/ads.ipynb) - notebook will eda and ab test analysis
  - [plots.py](https://github.com/aprilhong/ads_abtest/blob/main/plots.py) - module for various plots
</details>

### Technologies Used

<details> <Summary>Expand/Collapse</summary>
  
- Python
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Scikit-Learn
</details>

# Executive Summary


## Exploratory Data Analysis
<details><summary>Expand/Collapse</summary>
The dataset and business case is from [Kaggle](https://www.kaggle.com/datasets/faviovaz/marketing-ab-testing). The majority of the people will be exposed to ads (the experimental group). And a small portion of people (the control group) would instead see a Public Service Announcement (PSA) (or nothing) in the exact size and place the ad would normally be.
  
and stores information for 10,000 bank customers, with each customer represented by a row and 14 features in separate columns. This totals 140,000 data points.


![image](https://github.com/aprilhong/bankchurn/assets/78663820/b14a1a4b-c1d3-481c-b642-8d083ed23abe)


### Descriptive Statistics


### Data Cleaning


### Variable Analysis and Visualization

#### `Exited`


#### `Age`

<img src="https://github.com/aprilhong/bankchurn/assets/78663820/d693e2bd-97e4-4650-8ead-9b163d6581d3" width="400" >


<img src="https://github.com/aprilhong/bankchurn/assets/78663820/139d66ca-a226-465a-845a-5607f6aa95ee" width="500" >


#### `Balance`


#### `Active Members`


#### `Number Of Products`


#### `Geography`

#### Recommendations


### Future Improvements


</details>


