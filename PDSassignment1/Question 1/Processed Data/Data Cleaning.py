import pandas as pd

# Load the data into a DataFrame
df = pd.read_csv("data.csv")

# Remove any rows with missing values
df.dropna(inplace=True)

# Remove any duplicates
df.drop_duplicates(inplace=True)

# Convert the 'Frailty' column to boolean
df['Frailty'] = df['Frailty'].map({'Y': True, 'N': False})

# Convert the data types for the other columns as needed
df['Height (Inches)'] = df['Height (Inches)'].astype(float)
df['Weight (Pounds)'] = df['Weight (Pounds)'].astype(float)
df['Age'] = df['Age'].astype(int)
df['Grip strength'] = df['Grip strength'].astype(int)

# Create a new column for BMI
df['BMI'] = df['Weight (Pounds)'] / (df['Height (Inches)'] ** 2) * 703

# Save the cleaned data to a new file
df.to_csv("cleaned_data.csv", index=False)
