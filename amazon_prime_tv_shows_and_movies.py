# -*- coding: utf-8 -*-
"""Amazon Prime TV Shows and Movies.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EQmVtfRojG_7jypXXGgXxTajUnWXedox

# **Project Name**    - Amazon Prime TV Shows and Movies
"""



"""##### **Project Type**    - EDA
##### **Contribution**    - Individual

# **Project Summary -**

Write the summary here within 500-600 words.

**Business Context**  
In today’s competitive streaming environment, platforms like Amazon Prime Video continuously expand their content libraries to attract a diverse global audience. This project involves an in-depth analysis of the content available in the United States, using a dataset that combines both categorical and numerical data from two CSV files. The aim is to extract actionable insights that can help businesses, content creators, and data analysts understand audience preferences, trends, and effective content strategies.

**Dataset Overview**  
- **titles.csv:**  
  - Contains over 9,000 unique titles with 15 attributes.  
  - Key columns include:  
    - *id, title, show_type, description*  
    - *release_year, age_certification, runtime, genres*  
    - *production_countries, seasons, imdb_id, imdb_score, imdb_votes, tmdb_popularity, tmdb_score*
- **credits.csv:**  
  - Contains over 124,000 entries detailing cast and crew information.  
  - Key columns include:  
    - *person_ID, id, name, character_name, role*  
  - The role is categorized as either ACTOR or DIRECTOR.

**Analytical Objectives**  
- **Content Diversity:**  
  - Identify dominant genres and content types.  
  - Highlight niche areas that may drive unique audience engagement.
- **Regional Availability:**  
  - Analyze production countries to understand geographic trends.  
  - Assess opportunities for localized content strategies.
- **Trends Over Time:**  
  - Examine the evolution of Amazon Prime Video’s library via release years.  
  - Compare historical growth patterns and shifts in content strategy.
- **IMDb Ratings & Popularity:**  
  - Evaluate titles based on IMDb scores, votes, and TMDB popularity.  
  - Pinpoint which titles resonate best with audiences.

**Methodology and Tools**  
- **Pandas:**  
  - For data manipulation, merging, and aggregation of both CSV files.
- **NumPy:**  
  - To perform computationally efficient operations and statistical analysis.
- **Visualization:**  
  - **Matplotlib and Seaborn:**  
    - Create at least five distinct visualizations such as:
      - **Bar Charts:** Displaying genre distribution.
      - **Line Plots:** Illustrating trends over time.
      - **Heatmaps:** Highlighting correlations among performance metrics.
      - **Scatter Plots:** Exploring the relationship between IMDb and TMDB scores.
      - **Pie or Stacked Bar Charts:** Visualizing regional distribution.

**Insights and Impact**  
The analysis reveals multifaceted insights:  
- It clarifies which genres dominate the platform.  
- It exposes regional production trends and the evolution of the content library over time.  
- It identifies high-performing titles based on audience ratings and popularity.  

These insights empower stakeholders to optimize content offerings, fine-tune marketing strategies, and ultimately drive subscription growth in an increasingly competitive streaming market. This project not only underscores the importance of data-driven decision-making but also provides a robust framework for strategic content investment and audience engagement.

# **GitHub Link -**

Provide your GitHub Link here.
"""



"""# **Problem Statement**

This dataset was created to analyze all shows available on Amazon Prime Video, allowing us to extract valuable insights such as:

1. Content Diversity: What genres and categories dominate the platform?
2. Regional Availability: How does content distribution vary across different regions?
3. Trends Over Time: How has Amazon Prime’s content library evolved?
4. IMDb Ratings & Popularity: What are the highest-rated or most popular shows on the platform?
By analyzing this dataset, businesses, content creators, and data analysts can uncover key trends that influence subscription growth, user engagement, and content investment strategies in the streaming industry.

#### **Define Your Business Objective?**

In the rapidly evolving streaming industry, platforms like Amazon Prime Video face intense competition as they strive to attract and retain a diverse audience. This project leverages a comprehensive dataset encompassing over 9,000 unique titles and 124,000 credits to gain critical insights into content diversity, regional production trends, and viewer engagement metrics. By analyzing this data, stakeholders can identify which genres and regions are most influential, optimize content investments, and refine marketing strategies. Ultimately, these data-driven insights enable Amazon Prime Video to enhance its content strategy, drive subscription growth, and maintain a competitive edge in the dynamic digital entertainment landscape.

# **General Guidelines** : -

1.   Well-structured, formatted, and commented code is required.
2.   Exception Handling, Production Grade Code & Deployment Ready Code will be a plus. Those students will be awarded some additional credits.
     
     The additional credits will have advantages over other students during Star Student selection.
       
             [ Note: - Deployment Ready Code is defined as, the whole .ipynb notebook should be executable in one go
                       without a single error logged. ]

3.   Each and every logic should have proper comments.
4. You may add as many number of charts you want. Make Sure for each and every chart the following format should be answered.
        

```
# Chart visualization code
```
            

*   Why did you pick the specific chart?
*   What is/are the insight(s) found from the chart?
* Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

5. You have to create at least 20 logical & meaningful charts having important insights.


[ Hints : - Do the Vizualization in  a structured way while following "UBM" Rule.

U - Univariate Analysis,

B - Bivariate Analysis (Numerical - Categorical, Numerical - Numerical, Categorical - Categorical)

M - Multivariate Analysis
 ]

# ***Let's Begin !***

## ***1. Know Your Data***

### Import Libraries
"""

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""### Dataset Loading"""

# Load Dataset
from google.colab import drive
drive.mount('/content/drive')

"""### Dataset First View"""

# Dataset First Look
df = pd.read_csv('/content/drive/MyDrive/Almabetter DS Projects/Amazon TV shows and movies/credits.csv')
df.tail()

"""### Dataset Rows & Columns count"""

# Dataset Rows & Columns count
df_rows = df.shape[0]
df_cols = df.shape[1]

# Printing Rows and Columns
print(f"Number of rows: {df_rows}")
print(f"Number of columns: {df_cols}")

"""### Dataset Information"""

# Dataset Info
df.info()

"""#### Duplicate Values"""

# Dataset Duplicate Value Count
df.duplicated().sum()

"""#### Missing Values/Null Values"""

# Missing Values/Null Values Count
df.isnull().sum()

# Visualizing the missing values
df.isnull().sum().plot.bar()

"""### What did you know about your dataset?

### 1. Mounting Google Drive
I got to know how to mount my google drive using google.colab

### 2. Importing the Dataset
The dataset is imported using `pd.read_csv()` from its location in my Drive.

### 3. Shape of the Dataset
`df.shape` returns the number of rows and columns, which helps me understand the size and scope of the data.

### 4. Dataset Information
`df.info()` provides a concise summary of the DataFrame, including each column's data type and the count of non-null values. This is useful for detecting columns with missing data or unexpected data types.

### 5. Duplicate Rows
`df.duplicated().sum()` counts the number of duplicate rows, which is important to identify any redundancy in my data.

### 6. Missing Values
`df.isnull().sum()` calculates the total number of missing (null) values in each column, enabling me to plan data cleaning steps as needed.

### 7. Plot Null Values

`df.isnull().sum().plot().bar()` displays graphical representation of bar of missing/null values in each column

## ***2. Understanding Your Variables***
"""

# Dataset Columns
df.columns

# Dataset Describe
df.describe()

"""### Variables Description

### 1. Column Names
`df.columns` returns a list of all column names present in the dataset. This helps in understanding the available features and their naming conventions.

### 2. Statistical Summary
`df.describe()` provides a statistical summary of numerical columns, including:
- **Count**: Number of non-null values.
- **Mean**: Average value.
- **Standard Deviation (std)**: Measure of variability.
- **Min & Max**: Minimum and maximum values in the column.
- **25th, 50th (Median), 75th Percentiles**: Distribution of values in the dataset.

This function is useful for identifying trends, outliers, and the overall distribution of data.

### Check Unique Values for each variable.
"""

# Check Unique Values for each variable.
df.nunique()

"""## 3. ***Data Wrangling***

### Data Wrangling Code
"""

# Write your code to make your dataset analysis ready.
# Data collection, Data cleaning, Data transformation, Data merging and Integration, Data enrichement, Data validation, Data visualization

"""### Step 1: Load the Dataset"""

# Import necessary libraries:
import pandas as pd
import numpy as np
from google.colab import drive

# Read the dataset
drive.mount('/content/drive')
df = pd.read_csv('/content/drive/MyDrive/Almabetter DS Projects/Amazon TV shows and movies/titles.csv')

"""### Step 2: Understand the Data"""

# Get basic information:
df.info()
df.head()

# Check for missing values:
df.isnull().sum()

"""### Step 3: Handle Missing Values"""

# Drop missing values:
df.dropna(inplace=True)

# Check if any NaN values remain
df.isnull().sum() # Should return 0 for all columns if all NaNs were removed

# Fill missing values:
df.ffill(inplace=True)  # Forward fill

"""### Step 4: Handle Duplicate Data"""

# Check and remove duplicates
df.duplicated().sum()
df.drop_duplicates(inplace=True)

df.head()

"""### Step 5: Handle Incorrect Data Types"""

# Check the data type
df['seasons'].dtype

# Convert data type
df['total_seasons'] = df['seasons'].astype(int)

df.head()

"""### Step 6: Rename Columns"""

df.rename(columns={'id': 'movie_id', 'title': 'movie_title'}, inplace=True)

df.tail(1)

"""### Step 7: Feature Engineering"""

df['overall_rating'] = (df['imdb_score'] + df['tmdb_score']) / 2
df.head(5)

"""### Step 8: Save the Cleaned Data"""

df.to_csv("/content/drive/MyDrive/Almabetter DS Projects/Amazon TV shows and movies/cleaned_dataset.csv", index=True)

"""### What all manipulations have you done and insights you found?

1️⃣ Data Manipulations Performed
Here’s a structured breakdown of the manipulations I performed on the dataset:

🔹 Data Cleaning

✅ Handled Missing Values

Dropped missing values in non-critical columns.

Used forward fill (ffill) for time-series data.

✅ Removed Duplicates

Identified and deleted duplicate rows.

✅ Fixed Data Types

Converted seasons columns float to int type for efficient memory usage.

🔹 Data Transformation & Feature Engineering

✅ Renamed Columns

Standardized column names for better readability.

✅ Created New Features

Generated New overall ratings column which is an average of imdb_score and tmdb_score for understanding better reach of every show.

## ***4. Data Vizualization, Storytelling & Experimenting with charts : Understand the relationships between variables***

#### Chart - 1
"""

# Chart - 1 visualization code
df['release_year'].value_counts().plot(kind='bar')
plt.title('Bar Chart Example')
plt.show()
# df

"""##### 1. Why did you pick the specific chart?

Answer Here.

##### 2. What is/are the insight(s) found from the chart?

Answer Here

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here

#### Chart - 2
"""

# Chart - 2 visualization code

"""##### 1. Why did you pick the specific chart?

Answer Here.

##### 2. What is/are the insight(s) found from the chart?

Answer Here

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here

#### Chart - 3
"""

# Chart - 3 visualization code

"""##### 1. Why did you pick the specific chart?

Answer Here.

##### 2. What is/are the insight(s) found from the chart?

Answer Here

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here

#### Chart - 4
"""

# Chart - 4 visualization code

"""##### 1. Why did you pick the specific chart?

Answer Here.

##### 2. What is/are the insight(s) found from the chart?

Answer Here

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here

#### Chart - 5
"""

# Chart - 5 visualization code

"""##### 1. Why did you pick the specific chart?

Answer Here.

##### 2. What is/are the insight(s) found from the chart?

Answer Here

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here

#### Chart - 6
"""

# Chart - 6 visualization code

"""##### 1. Why did you pick the specific chart?

Answer Here.

##### 2. What is/are the insight(s) found from the chart?

Answer Here

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here

#### Chart - 7
"""

# Chart - 7 visualization code

"""##### 1. Why did you pick the specific chart?

Answer Here.

##### 2. What is/are the insight(s) found from the chart?

Answer Here

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here

#### Chart - 8
"""

# Chart - 8 visualization code

"""##### 1. Why did you pick the specific chart?

Answer Here.

##### 2. What is/are the insight(s) found from the chart?

Answer Here

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here

#### Chart - 9
"""

# Chart - 9 visualization code

"""##### 1. Why did you pick the specific chart?

Answer Here.

##### 2. What is/are the insight(s) found from the chart?

Answer Here

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here

#### Chart - 10
"""

# Chart - 10 visualization code

"""##### 1. Why did you pick the specific chart?

Answer Here.

##### 2. What is/are the insight(s) found from the chart?

Answer Here

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here

#### Chart - 11
"""

# Chart - 11 visualization code

"""##### 1. Why did you pick the specific chart?

Answer Here.

##### 2. What is/are the insight(s) found from the chart?

Answer Here

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here

#### Chart - 12
"""

# Chart - 12 visualization code

"""##### 1. Why did you pick the specific chart?

Answer Here.

##### 2. What is/are the insight(s) found from the chart?

Answer Here

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here

#### Chart - 13
"""

# Chart - 13 visualization code

"""##### 1. Why did you pick the specific chart?

Answer Here.

##### 2. What is/are the insight(s) found from the chart?

Answer Here

##### 3. Will the gained insights help creating a positive business impact?
Are there any insights that lead to negative growth? Justify with specific reason.

Answer Here

#### Chart - 14 - Correlation Heatmap
"""

# Correlation Heatmap visualization code

"""##### 1. Why did you pick the specific chart?

Answer Here.

##### 2. What is/are the insight(s) found from the chart?

Answer Here

#### Chart - 15 - Pair Plot
"""

# Pair Plot visualization code

"""##### 1. Why did you pick the specific chart?

Answer Here.

##### 2. What is/are the insight(s) found from the chart?

Answer Here

## **5. Solution to Business Objective**

#### What do you suggest the client to achieve Business Objective ?
Explain Briefly.

Answer Here.

# **Conclusion**

Write the conclusion here.

### ***Hurrah! You have successfully completed your EDA Capstone Project !!!***
"""