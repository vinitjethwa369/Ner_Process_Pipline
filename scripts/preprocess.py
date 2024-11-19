import pandas as pd
import os

def preprocess_data(input_path, output_path):
    print("Starting preprocessing...")

    # Load the data
    df = pd.read_csv(input_path)
    print(f"Loaded data with {len(df)} rows.")

    # Ensure the column name is 'Description'
    if 'Description' not in df.columns:
        raise ValueError("The file must have a column named 'Description'.")

    # Cleaning steps
    df['CleanDescription'] = df['Description'].str.replace(r'[^a-zA-Z\s]', ' ', regex=True)  # Remove digits and special characters
    df['CleanDescription'] = df['CleanDescription'].str.replace(r'[xX]+', '', regex=True)   # Remove occurrences of 'x' or 'X'
    df['CleanDescription'] = df['CleanDescription'].str.replace(r'\s+', ' ', regex=True).str.strip()  # Normalize spaces

    # Extract the first word
    df['Name'] = df['CleanDescription'].str.split().str[0]

    # Save cleaned data
    df[['Description', 'CleanDescription', 'Name']].to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")
    return output_path

if __name__ == "__main__":
    input_file = "data/input_data.csv"
    output_file = "data/cleaned_data.csv"
    os.makedirs("data", exist_ok=True)
    preprocess_data(input_file, output_file)
