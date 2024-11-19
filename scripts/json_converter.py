import pandas as pd
import json
import os

def prepare_json(input_csv_path, output_json_path):
    print("Converting CSV to JSON for training...")

    df = pd.read_csv(input_csv_path)
    json_output = []
    id_start = 10000  # Starting ID

    for idx, row in df.iterrows():
        text = str(row['Description']).strip()
        if 'Name' in row:
            name = str(row['Name']).strip()
            if name and name.lower() in text.lower():
                start_idx = text.lower().find(name.lower())
                end_idx = start_idx + len(name)
                json_output.append({
                    "id": id_start + idx,
                    "data": {"text": text},
                    "annotations": [{
                        "result": [{
                            "id": "annotation_id",
                            "type": "labels",
                            "value": {"start": start_idx, "end": end_idx, "text": text[start_idx:end_idx], "labels": ["Beneficiary Name"]}
                        }]
                    }]
                })
        else:
            print(f"Skipping row {idx}: 'Name' column is missing or empty.")

    # Save JSON file
    with open(output_json_path, 'w') as outfile:
        json.dump(json_output, outfile, indent=4)
    print(f"Training JSON saved to {output_json_path}")
    return output_json_path

if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)
    prepare_json("data/shuffled_data.csv", "output/training_data.json")
