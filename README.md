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
  
The dataset and business case is from [Kaggle](https://www.kaggle.com/datasets/faviovaz/marketing-ab-testing). The majority of the people will be exposed to ads (the experimental group). And a small portion of people (the control group) would instead see a Public Service Announcement (PSA) (or nothing) in the exact size and place the ad would normally be.

### Assumptions (on Success metric)
Since no success criteria was provided, an assumption was made for the campaign's success criteria. The campaign is considered **successful** if conversion rate in ad group is at least **20% higher** than psa group.

### Load Dataset
<img src="https://github.com/aprilhong/ads_abtest/assets/78663820/f20948be-9340-4fe3-a629-af4b08729a9d" width="600" >


#### Data Dictionary

<img src="https://github.com/aprilhong/ads_abtest/assets/78663820/a2b5d9bf-b65d-491b-bca8-dc2719372bad" width="600" >


#### Basic Info

<img src="https://github.com/aprilhong/ads_abtest/assets/78663820/dbc3bdf3-79c4-47bd-9cf8-7f10aabe772a" width="400" >

<br>
<br>

- dataset has a total of 588101 rows and 6 columns
- each row represents a viewer
- each column displays the viewer's ad experience
- 3 Categorical Variables: test group, converted, most ads day 
- 3 Numerical Variables: user id, total ads,most ads hour 
- There are no null values 

### Descriptive Statistics

<img src="https://github.com/aprilhong/ads_abtest/assets/78663820/21df8b0a-c16d-46ac-b88a-bfa761da6fd4" width="600" >

<br>
<br>

User Id
- There are a total of 588,101 users included in this data set.

Test Group
- The data consists of users from two different test groups.
- The majority of users (564,577) belong to the ad group.

Converted
- There are two conversion categories: "True" for those who purchased the product and "False" for those who didn't.
- The majority of users (approximately 97%) fall under the "False" category, meaning they haven't converted yet. 
- This suggests a low conversion rate overall.

Total Ads (watched by a user)
- On average, users watch nearly 25 ads.
- However, the median is only 13 ads, indicating that a small number of users watch a very high number of ads, skewing the average.
- The maximum number of ads watched by a single user is 2,065, further supporting the rightward skew in the data.

Most Ads (watched per) Day
- Data for seven days of the week is included (presumably Monday through Sunday).
- Friday is the day when users watch the most ads on average.

Most Ads (watched per) Hour
- The average number of ads watched per hour (14.5) is close to the median (14), suggesting a relatively balanced distribution of ad watching throughout the day.

### Data Cleaning

#### Check for outliers

<img src="https://github.com/aprilhong/ads_abtest/assets/78663820/c6915200-c457-4e1b-b31b-41d613fc25c2" width="600" >

total_ads
- LL: -30.5 | UL: 61.5
- Rows of outliers : 52057
- Percent outliers : 8.85%

most_ads_hour
- LL: 0.5 | UL: 28.5
- Rows of outliers : 5536
- Percent outliers : 0.94%

<br>

- there's a relatively high number of outliers for the `total_ads` feature. These outliers represent approximately 9% of the total data, which is quite substantial.
- In contrast, the most_ads_hour has a much lower proportion of outliers, only around 0.94% of the total data


### Variable Analysis and Visualization

#### `test group`
<img src="https://github.com/aprilhong/ads_abtest/assets/78663820/fc36e42e-1c23-41e8-a8ef-98e925417b1c" width="400" >

- the 2 test groups are: ad and psa
- 96% of viewers belong to the Ad group.
- Around 14,000 viewers purchased the product after seeing the Ad.
- Only 420 viewers purchased from the PSA group.

**Calculate the conversion rate for each group**

```python
# save test_group values to list
groups = df['test_group'].unique().tolist()

# Calculate conversion in each test group
def calculate_conversion_rate_difference(df, groups):
  """
  This function calculates the conversion rate for each group in the provided DataFrame 'df' 
  and the difference in conversion rate between consecutive groups specified in 'groups' list.

      df (pandas.DataFrame): The DataFrame containing 'test_group' and 'converted' columns.
      groups (list): A list containing the group names for which conversion rates are to be calculated.

  Returns:
      None: The function prints the conversion rate for each group and the difference between it and the previous group's rate.
  """

  prev_percent_convert = None

  for group in groups:
    count = df[(df['test_group'] == group)].shape[0]
    convert_count = df[(df['test_group'] == group) & (df['converted'] == True)].shape[0]
    percent_convert = (convert_count / count) * 100
    print(f'Conversion rate in {group} group:  {percent_convert:.2f}%')

    if prev_percent_convert is not None:
      percent_difference = ((prev_percent_convert-percent_convert)/percent_convert) *100
      print(f'% Difference between the conversion rates: {percent_difference:.1f}%')

    prev_percent_convert = percent_convert

# apply function
calculate_conversion_rate_difference(df.copy(), groups.copy())
```
<br>

- Conversion rate in ad group:  2.55%
- Conversion rate in psa group:  1.79%
- % Difference between the conversion rates: 43.1%

Our analysis revealed that viewers who watched the advertisement (Ad group) achieved a conversion rate **43% higher** compared to the Public Service Announcement (PSA group).

**Success Criteria:** We previously defined a success criterion for this campaign: the Ad group's conversion rate should be at least 20% higher than the PSA group.

**Result:** Since the Ad group's conversion rate surpasses the 20% threshold, exceeding it by an impressive 43%, we can confidently conclude that this campaign is a success!

#### `converted`

<img src="https://github.com/aprilhong/ads_abtest/assets/78663820/8e446ac6-9b44-4fd4-b9b6-2d79d77c2b1f" width="300" >

- False indicate the viewers did not purchase the product
- While a significant portion (93.5%) of users saw the ads, the actual purchase rate was low. 
- Only 2.5% of viewers converted into paying customers.


#### `total ads (watched)`

<img src="https://github.com/aprilhong/ads_abtest/assets/78663820/e5a34ac5-da06-446d-b4c2-25a7f469c9e4" width="600" >

- most viewers watch 1-5 ads in total
- 96% of viewers watch less than 104 ads in total 
- less than 0.01% watch over 1033 ads

#### `most_ads_day`

<img src="https://github.com/aprilhong/ads_abtest/assets/78663820/b39c35b4-fac7-4f39-91cd-3be7fc8e9eae" width="600" >

- Ad engagement is fairly consistent throughout the weekdays, with Fridays seeing a slight bump (15.7%) and Tuesdays seeing a slight dip (13.2%). 
- Overall, ad viewership falls within a narrow range of 13% to 15.7% across all days.

**Conversion rate per day**

<img src="https://github.com/aprilhong/ads_abtest/assets/78663820/84cbc761-6b31-454e-998c-e7c2c77cba65" width="600" >

- Conversion rates remain consistently low across all days of the week
- Monday has the highest rate at a modest 3.3% 
- Saturdays see the lowest conversion rate at just 2.1%
  
#### `most_ads_hour`

<img src="https://github.com/aprilhong/ads_abtest/assets/78663820/ff078ad1-6f6f-4db1-9479-d2fd8509e274" width="600" >

- Ad viewership are highest around noon time (11AM-3PM), potentially coinciding with lunchtime breaks.
- Engagement remains low throughout the overnight hours (12:00 AM to 7:00 AM) as viewers are probably asleep.



#### Recommendations


### Future Improvements




