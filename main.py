import pandas as pd

# Load datasets
responses_2021 = pd.read_csv('Datasets/survey_results_2021.csv')
responses_2023 = pd.read_csv('Datasets/survey_results_2023.csv')

# Step 1: Filter out rows where the "MainBranch" column is not "I am a developer by profession"
responses_2021_filtered = responses_2021[responses_2021['MainBranch'] == "I am a developer by profession"]
responses_2023_filtered = responses_2023[responses_2023['MainBranch'] == "I am a developer by profession"]

# Step 2: Drop irrelevant columns (including the additional columns you want to remove)
columns_to_drop_2021 = ['US_State', 'UK_Country', 'Country']  # Add other irrelevant columns if needed
columns_to_drop_2023 = ['US_State', 'UK_Country', 'Country',
                        'Knowledge_1', 'Knowledge_2', 'Knowledge_3',
                        'Knowledge_4', 'Knowledge_5', 'Knowledge_6',
                        'Knowledge_7', 'Knowledge_8', 'Frequency_1',
                        'Frequency_2', 'Frequency_3', 'TimeSearching',
                        'TimeAnswering', 'ProfessionalTech', 'Industry',
                        'SurveyLength', 'SurveyEase']

# Drop irrelevant columns from both datasets
responses_2021_cleaned = responses_2021_filtered.drop(columns=columns_to_drop_2021, errors='ignore')
responses_2023_cleaned = responses_2023_filtered.drop(columns=columns_to_drop_2023, errors='ignore')

# Step 3: Handle missing data
# Drop rows with missing values in key columns like 'LanguageHaveWorkedWith' and 'ConvertedCompYearly'
responses_2021_cleaned = responses_2021_cleaned.dropna(subset=['LanguageHaveWorkedWith', 'ConvertedCompYearly'])
responses_2023_cleaned = responses_2023_cleaned.dropna(subset=['LanguageHaveWorkedWith', 'ConvertedCompYearly'])

# Step 4: Standardize column names (if necessary)
responses_2021_cleaned.rename(columns={'LanguageHaveWorkedWith': 'Languages'}, inplace=True)
responses_2023_cleaned.rename(columns={'LanguageHaveWorkedWith': 'Languages'}, inplace=True)

# Step 5: Explode the 'Languages' column to separate each language into its own row
responses_2021_expanded = responses_2021_cleaned.assign(Languages=responses_2021_cleaned['Languages'].str.split(';')).explode('Languages')
responses_2023_expanded = responses_2023_cleaned.assign(Languages=responses_2023_cleaned['Languages'].str.split(';')).explode('Languages')

# Save cleaned datasets if needed
responses_2021_expanded.to_csv('cleaned_2021_survey_responses.csv', index=False)
responses_2023_expanded.to_csv('cleaned_2023_survey_responses.csv', index=False)

# Print the shapes of the cleaned datasets
print(f"2021 Cleaned Shape: {responses_2021_expanded.shape}")
print(f"2023 Cleaned Shape: {responses_2023_expanded.shape}")
