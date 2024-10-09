import pandas as pd

# Load datasets
responses_2021 = pd.read_csv('Datasets/survey_results_2021.csv')
responses_2023 = pd.read_csv('Datasets/survey_results_2023.csv')

# Filter out rows where the "MainBranch" column is not "I am a developer by profession"
responses_2021_filtered = responses_2021[responses_2021['MainBranch'] == "I am a developer by profession"]
responses_2023_filtered = responses_2023[responses_2023['MainBranch'] == "I am a developer by profession"]

# Optionally, save the filtered datasets to new CSV files
responses_2021_filtered.to_csv('filtered_2021_survey_responses.csv', index=False)
responses_2023_filtered.to_csv('filtered_2023_survey_responses.csv', index=False)

# Print the shape of the filtered datasets to confirm
print(f"2021 Filtered Shape: {responses_2021_filtered.shape}")
print(f"2023 Filtered Shape: {responses_2023_filtered.shape}")
