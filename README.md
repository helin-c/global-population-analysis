# GlobalTech: Python Population Demographics Analysis

## 🌍 Project Overview
This project was completed as a technical delivery task for a Data Analyst application at GlobalTech, a company that contracts for data analysis with government departments. The objective was to analyze a dataset (`population.csv`) containing global population statistics across multiple years using Python.

## 🛠️ Tools & Techniques
* **Python:** Core language used for the entire analysis.
* **Pandas:** Utilized for data loading, cleaning, filtering, reshaping, and mathematical manipulation.
* **Matplotlib:** Used to generate visual insights, including bar charts, scatter plots, and line graphs.
* **Data Cleaning & Preparation:** The dataset was first inspected for missing values, duplicates, and data type issues. There were 8 rows found that contained missing (NaN) values in the population column. These rows were removed before analyzing, as missing population values would misrepresent calculations involving totals, averages, and growth rates. Population values recorded as zero were intentionally retained, as they represent recorded data rather than missing entries, and no duplicate rows were identified.

## 📊 Key Findings & Visualizations

### 1. Missing Population Data (2000)
**Question:** How many countries had no recorded population data (0) for the year 2000? 
* **Insight:** There were 59 countries that had a recorded population value of 0. These locations are mainly small island nations, overseas territories, or regions that may have limited data reporting at the start of the decade. The original dataset was used rather than the cleaned dataset for this specific query, as the question required identifying recorded population values of zero, which were treated as valid recorded data rather than missing values.

### 2. African Population Distribution (2010)
**Question:** Calculate the total population for all African countries in 2010 and create a bar chart showing the distribution.
* **Insight:** The total population for African countries in 2010 was 991.0 million. A bar chart was created to show the population distribution across African countries, sorted by population size to improve readability. The chart highlights the highly uneven distribution across the continent: a small number of countries (like Nigeria) account for a massive proportion of the total population, while many remain below 20 million.

![African Population Distribution](https://github.com/helin-c/global-population-analysis/blob/main/Q2.png?raw=true)

### 3. South American Population Skew (2000)
**Question:** Determine the average population of countries in South America for the year 2000 and highlight countries above and below this average.
* **Insight:** The average population was 24.50 million. Only 4 countries (Argentina, Brazil, Colombia, Peru) were above this average, while 10 countries fell below it (Bolivia, Chile, Ecuador, Falkland Islands, French Guiana, Guyana, Paraguay, Suriname, Uruguay, Venezuela). This split indicates a strong right-skew in the data, largely driven by Brazil’s massive population, which pulls the overall average up significantly and causes the vast majority of countries (10 out of 14) to fall below the mean.

### 4. The 1 Billion Population Threshold (2007)
**Question:** Identify the countries with populations exceeding 1000 million in 2007.
* **Insight:** Only China (1,310.0 million) and India (1,124.0 million) exceeded the 1,000 million population threshold in 2007. Two scatter plots were created to visualize this result. The first plot displayed all countries ranked by population to avoid overcrowding on the x-axis, clearly highlighting China and India as extreme outliers. A second scatter plot focused strictly on the top 20 countries, allowing country names to be shown and making it easier to identify which countries are closer to, but do not exceed, the threshold.

![Top 20 Scatter Plots](https://github.com/helin-c/global-population-analysis/blob/main/Q4.2.png?raw=true)

### 5. European Population Growth (2000-2010)
**Question:** Calculate the total population growth in Europe between 2000 and 2010 and identify the top 5 European countries by population growth.
* **Insight:** The data was grouped to isolate European nations and calculate the absolute growth between the start and end of the decade. A line plot was generated to track the specific growth trajectories of the top 5 fastest-growing European countries over this 10-year period.

![European Growth Line Plot](https://github.com/helin-c/global-population-analysis/blob/main/Q5.png?raw=true)

## 📂 Repository Contents
* `global population analysis.py`: The complete Python script containing all data manipulation and visualization code.
* `population.csv`: The core dataset used for this analysis.
