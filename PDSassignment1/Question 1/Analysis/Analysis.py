import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data into a DataFrame
df = pd.read_csv("cleaned_data.csv")

# Compute summary statistics for the data
print(df.describe())

# Compute pairwise correlations between the columns
print(df.corr())

# Create a histogram of the 'Age' column
sns.histplot(data=df, x='Age')
plt.show()

# Create a scatter plot of 'Weight' vs. 'Height'
sns.scatterplot(data=df, x='Height (Inches)', y='Weight (Pounds)', hue='Frailty')
plt.show()

# Create a box plot of 'Grip strength' by 'Frailty'
sns.boxplot(data=df, x='Frailty', y='Grip strength')
plt.show()

# Create a violin plot of 'BMI' by 'Frailty'
sns.violinplot(data=df, x='Frailty', y='BMI')
plt.show()

# Create a pair plot of all numerical columns
sns.pairplot(data=df, hue='Frailty')
plt.show()
