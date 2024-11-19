import pandas as pd
import os
from sklearn.utils import shuffle

def sample_data(input_path, output_path, n=500):
    print("Starting sampling...")

    df = pd.read_csv(input_path)
    unique_keys = df['Name'].unique()
    sampled_data = pd.DataFrame()

    for key in unique_keys:
        key_data = df[df['Name'] == key]
        key_sampled = key_data.sample(n=min(n, len(key_data)), random_state=42)
        sampled_data = pd.concat([sampled_data, key_sampled])

    # Save sampled data
    sampled_data.to_csv(output_path, index=False)
    print(f"Sampled data saved to {output_path} with {len(sampled_data)} rows.")
    return output_path

def shuffle_data(input_path, output_path):
    print("Starting shuffling...")

    # Load and shuffle data
    data = pd.read_csv(input_path)
    shuffled_data = shuffle(data, random_state=42).reset_index(drop=True)

    # Save shuffled data
    shuffled_data.to_csv(output_path, index=False)
    print(f"Shuffled data saved to {output_path}")
    return output_path

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    sampled_file = "data/sampled_data.csv"
    shuffled_file = "data/shuffled_data.csv"

    # Sample and shuffle
    sample_data("data/cleaned_data.csv", sampled_file)
    shuffle_data(sampled_file, shuffled_file)
