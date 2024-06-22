# Advanced Wrangling With Pandas
## Resource Information: https://www.tomasbeuzen.com/python-programming-for-data-science/practice-exercises/chapter9-wrangling-advanced-practice.html
## This practice contains a list of questions which are being answered right below.
## The answers have to be generated for the requestor from the dataframe and display the data efficiently and effectively


import pandas as pd

# URL of the dataset
url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-14/passwords.csv'

# Specify the columns to import
columns_to_import = ['password', 'value', 'time_unit']

# Read the CSV file directly from the URL with specific columns
df = pd.read_csv(url, usecols=columns_to_import)

# Display the first few rows of the dataframe
print('Original Dataset')
print(df.head())


# Convert all the time unit to hours for standardisation
# Define a mapping of time units to their equivalent in hours
units = {
    'seconds': 1/3600,
    'minutes': 1/60,
    'days': 24,
    'weeks': 168,
    'months': 720,
    'years': 8760   
}

# Function to convert value and time_unit to seconds
def convert_to_hours(row):
    return row['value'] * units.get(row['time_unit'], 1)

# Apply the conversion function to each row
df['value_in_hours'] = df.apply(convert_to_hours, axis=1)

# Display the first few rows of the dataframe with the new column
print("\nDataFrame with value converted to hours:")
print(df.head())

## How many passwords begin with sequence 123
# Drop rows where the 'password' column has NaN values
df = df.dropna(subset=['password'])

# Filter the dataframe for passwords that start with 123
passwords_starting_with_123 = df[df['password'].str.startswith('123')]

# Count the number of such passwords
passwords_starting_with_123_count = len(passwords_starting_with_123)
print ('\nNumber of passwords starting with 123:', passwords_starting_with_123_count)

## What is the average time in hours needed to crack these passwords that begin with 123? 
# Calculate the average time in hours to crack passwords starting with '123'
average_time_123 = passwords_starting_with_123['value_in_hours'].mean()
print('\nAverage time in hours to crack passwords starting with 123:', average_time_123, 'hours')

## How does this compare to the average of all passwords in the dataset?
# Calculate the average time in hours to crack all passwords
average_time_all = df['value_in_hours'].mean()
print('\nAverage time in hours to crack all passwords:', average_time_all, 'hours')

## How many passwords do not contain a number?



## How many passwords contain at least one number?


## Is there an obvious difference in online cracking time between passwords that don’t contain a number vs passwords that contain at least one number?


## How many passwords contain at least one of the following punctuations: [.!?\\-] (hint: remember this dataset contains weak passwords…)?


## Which password(s) in the datasets took the shortest time to crack by online guessing? Which took the longest?



