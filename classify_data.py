import pandas as pd
import os

# Define the classification rules
classification_rules = {
    "Sensitive": ["Name", "Gender", "Race", "Birthday", "Address", "Telephone", "Mobile", "Email (real)", "Blood Type", "Mother's Maiden Name"],
    "Confidential": ["Occupation", "Company Name", "Company Size", "Monthly Salary", "Security Answer"],
    "Public": ["Vehicle", "Website", "Favorite Color", "Favorite Movie", "Favorite Song", "Favorite Book", "Favorite Sports"],
    "Private": ["Username", "Password", "Password after MD5", "GUID", "Register IP", "Last Login IP", "Security Question"],
    "Critical": []  # Currently, no fields are classified as Critical
}

# Function to classify the data based on rules
def classify_data(row, classification_rules):
    classified_data = {"Sensitive": {}, "Confidential": {}, "Public": {}, "Private": {}, "Critical": {}}
    for category, fields in classification_rules.items():
        for field in fields:
            if field in row:
                classified_data[category][field] = row[field]
    return classified_data

# Load the dataset from a CSV file
df = pd.read_csv("dataset.csv")  # Replace "your_dataset.csv" with the path to your dataset file

# Create directory to save classified data
output_dir = "classified_data"
os.makedirs(output_dir, exist_ok=True)

# Initialize lists to store classified data
classified_sensitive = []
classified_confidential = []
classified_public = []
classified_private = []
classified_critical = []

# Classify each row in the dataset
for _, row in df.iterrows():
    classified = classify_data(row, classification_rules)
    
    classified_sensitive.append(classified['Sensitive'])
    classified_confidential.append(classified['Confidential'])
    classified_public.append(classified['Public'])
    classified_private.append(classified['Private'])
    classified_critical.append(classified['Critical'])

# Convert classified data to DataFrames
df_sensitive = pd.DataFrame(classified_sensitive)
df_confidential = pd.DataFrame(classified_confidential)
df_public = pd.DataFrame(classified_public)
df_private = pd.DataFrame(classified_private)
df_critical = pd.DataFrame(classified_critical)

# Save classified data to CSV files
df_sensitive.to_csv(os.path.join(output_dir, "classified_sensitive.csv"), index=False)
df_confidential.to_csv(os.path.join(output_dir, "classified_confidential.csv"), index=False)
df_public.to_csv(os.path.join(output_dir, "classified_public.csv"), index=False)
df_private.to_csv(os.path.join(output_dir, "classified_private.csv"), index=False)
df_critical.to_csv(os.path.join(output_dir, "classified_critical.csv"), index=False)

print("Data classification complete. Classified data saved to the 'classified_data' directory.")