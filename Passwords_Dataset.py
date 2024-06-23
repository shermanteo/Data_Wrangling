# Advanced Wrangling With Pandas


## This practice contains a dataset with a list of instructions on how the data should be presented and questions pertaining to the dataset.
## The answers have to be generated for the requestor from the dataframe and display the data efficiently and effectively

## Resource Information: https://www.tomasbeuzen.com/python-programming-for-data-science/practice-exercises/chapter9-wrangling-advanced-practice.html

# Advanced Wrangling With Pandas

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



## Convert all the time unit to hours for standardisation
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
# Filter passwords that do not contain any numbers using a regular expression
passwords_without_numbers = df[~df['password'].str.contains(r'\d', regex=True)]

# Count the number of such passwords
count_without_numbers = len(passwords_without_numbers)
print('\nThe number of passwords without numbers is:', count_without_numbers)



## How many passwords contain at least one number?
# Filter passwords that contain any numbers using a regular expression
passwords_with_numbers = df[df['password'].str.contains(r'\d', regex=True)]

# Count the number of such passwords
count_with_numbers = len(passwords_with_numbers)
print('\nThe number of passwords with at least one number is:', count_with_numbers)



## Is there an obvious difference in online cracking time between passwords that don’t contain a number vs passwords that contain at least one number?
# Calculate the average time in hours to crack passwords without numbers
average_time_without_numbers = passwords_without_numbers['value_in_hours'].mean()
print('\nAverage time in hours to crack passwords without numbers: ', average_time_without_numbers, 'hours')
# Calculate the average time in hours to crack passwords with numbers
average_time_with_numbers = passwords_with_numbers['value_in_hours'].mean()
print('\nAverage time in hours to crack passwords with numbers: ', average_time_with_numbers, 'hours')



## How many passwords contain at least one of the following punctuations: [.!?\\-] (hint: remember this dataset contains weak passwords…)?
# Filter passwords that contain any of the specified punctuations using a regular expression
punctuation_pattern = r'[.!?\\-]'
passwords_with_punctuations = df[df['password'].str.contains(punctuation_pattern, regex=True)]
# Count the number of such passwords
count_with_punctuations = len(passwords_with_punctuations)
print('\nNumber of passwords that contain at least one of the following punctuations [.!?\\-]: ', count_with_punctuations, 'passwords')



## Which password(s) in the datasets took the shortest time to crack by online guessing? Which took the longest?
# Find the row(s) with the shortest cracking time
shortest_time_row = df[df['value_in_hours'] == df['value_in_hours'].min()]
print("\nPassword(s) with the shortest time to crack:")
print(shortest_time_row[['password', 'value', 'time_unit', 'value_in_hours']])
# Find the row(s) with the longest cracking time
longest_time_row = df[df['value_in_hours'] == df['value_in_hours'].max()]
print("\nPassword(s) with the longest time to crack:")
print(longest_time_row[['password', 'value', 'time_unit', 'value_in_hours']])


