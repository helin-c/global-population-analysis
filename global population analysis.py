import pandas as pd 
import matplotlib.pyplot as plt

#Loading the dataset
population = pd.read_csv(r"C:\Generation Data Analyst Bootcamp\python\Python_Practical_task\population.csv")
print(population.head())

#check column names and data types: 
#print(population.info())

#check for missing vales per column:
print(population.isnull().sum())

#check for duplicate rows:
#print(population.duplicated().sum())

#The dataset contains 8 rows with missing (NaN) population values.
#These rows are removed to ensure calculations are accurate
population_clean = population.dropna(subset=["population"])


#Question 1
#How many countries had no recorded population data (0) for the year 2000?
#List these countries along with their continent. 

pop_data2000 = population[(population["year"] == 2000) & 
(population["population"] == 0)]

pop_list2000 = pop_data2000[["country name", "continent"]]
pop_count2000 = len(pop_list2000)
print(f" {pop_count2000} countries had no recorded population in 2000.")
print(pop_list2000)

#Question 2
#Total population for all African Countries in 2010. 
#Bar chart showing the population distribution across African countries in 2010

#Filtering for Africa and Year 2010 using the cleaned data
africa_2010 = population_clean[(population_clean["continent"] == "Africa")
& (population_clean["year"] == 2010)]

total_africa_pop = africa_2010["population"].sum()
print(f"Total african population in 2010: {total_africa_pop} million")

#Sorting data for a cleaner visual representation 
africa_2010_sorted = africa_2010.sort_values(by="population", ascending=False)
#Bar chart
plt.figure(figsize=(12,8))
plt.bar(africa_2010_sorted["country name"], africa_2010_sorted["population"])
plt.xticks(rotation=90)
plt.title("Population Distribution Across African Countries (2010)")
plt.xlabel("Country")
plt.ylabel("Population (Millions)")
plt.tight_layout()
plt.show()

#Question 3
#Average population of countries in South America in 2000.
#Highlight countries above & below the average 
sa_2000 = population_clean[(population_clean["continent"] == "South America") &
(population_clean["year"] == 2000)]

avg_sa_pop = sa_2000["population"].mean()

#Create lists of country names based on the average
above_avg = sa_2000[sa_2000["population"] > avg_sa_pop]["country name"].tolist()
below_avg = sa_2000[sa_2000["population"] <= avg_sa_pop]["country name"].tolist()

print(f"Average South American population in 2000: {avg_sa_pop:.2f} million")
print(f"Countries Above Average: {above_avg}")
print(f"Countries Below Average: {below_avg}")

#Question 4 
#Countries with populations exceeding 1000 million in 2007.

# Filter data for the year 2007
pop_2007 = population_clean[population_clean["year"] == 2007]
#Identify countries with population > 1000 million
over_1000 = pop_2007[pop_2007["population"] > 1000]
print("Countries exceeding 1000 million in 2007:")
print(over_1000[["country name", "population"]])

#Plot 1: Scatter Plot with all countries
#Sort countries by population for clearer visualisation
pop_2007_sorted = pop_2007.sort_values(by='population', ascending=False)
#Colour countries above 1000 million differently
colors = ['red' if x > 1000 else 'gray' for x in pop_2007_sorted["population"]]
#Create scatter plot using population rank on x-axis
plt.figure(figsize=(12, 6))
#using range for x-axis to fit all countries
plt.scatter(range(len(pop_2007_sorted)), pop_2007_sorted["population"], c=colors, alpha=0.5)
#Add reference line for 1000 million threshold
plt.axhline(y=1000, color='red', linestyle='--', label='1000M Threshold')

plt.title("Global Country Populations in 2007 (All Countries)")
plt.ylabel("Population (Millions)")
plt.xlabel("Country Rank (by Population)")
plt.legend()
plt.tight_layout()
plt.show()

#Plot 2: Top 20 Countries 
#Created a second plot to see the specific countries just below the 1000M
#threshold, as the first plot is overcrowded. 

top_20_2007 = pop_2007_sorted.head(20)
colors_top20 = ['red' if x > 1000 else 'blue' for x in top_20_2007["population"]]
plt.figure(figsize=(12, 6))
#using country names for x-axis since we only have 20 data points
plt.scatter(top_20_2007["country name"], top_20_2007["population"], 
c=colors_top20, s=100, alpha=0.5)
#Add reference line
plt.axhline(y=1000, color='red', linestyle='--', label='1000M Threshold')

plt.title("Top 20 Country Populations in 2007")
plt.ylabel("Population (Millions)")
plt.xlabel("Country")
plt.xticks(rotation=45, ha='right') #rotate names for readability
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.tight_layout()
plt.show()


#Question 5
#Total population growth in Europe between 2000 and 2010
europe = population_clean[population_clean["continent"] == "Europe"]

#Set index to 'country name' to allow direct subtraction of series
pop_2000 = europe[europe["year"] == 2000].set_index("country name")["population"]
pop_2010 = europe[europe["year"]== 2010].set_index("country name")["population"]

#calculating growth
growth = pop_2010 - pop_2000
total_growth = growth.sum()

top_5 = growth.sort_values(ascending=False).head(5)

print(f"Total European population growth: {total_growth} million")
print(f"Top 5 countries by growth: {top_5}")

#Line plot
plt.figure(figsize=(10, 6))
#Loop through the top 5 countries to plot seperate lines for each
for country in top_5.index:
    #Filter data for specific countries and sorted by year
    data = europe[europe["country name"] == country].sort_values(by="year")
    plt.plot(data["year"], data["population"], marker='o', label=country)
plt.legend()
plt.title("Population Growth of Top 5 European countries (2000-2010)")
plt.xlabel("Year")
plt.ylabel("Population")
plt.tight_layout()
plt.show()
