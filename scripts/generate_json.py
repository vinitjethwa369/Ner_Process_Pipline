import json
import pandas as pd

def generate_training_json(input_path, output_path):
    def validate_and_generate_json(row, id_start, project_id="ner_training_project"):
        text = str(row['Description']).strip()
        name = str(row.get('Name', '')).strip()
        if not name or name.lower() not in text.lower():
            return None
        start_idx = text.lower().find(name.lower())
        end_idx = start_idx + len(name)
        return {
            "id": id_start,
            "project_id": project_id,
            "data": {"text": text},
            "annotations": [{"result": [{"id": "annotation_id", "type": "labels", 
                                         "value": {"start": start_idx, "end": end_idx, 
                                                   "text": text[start_idx:end_idx], "labels": ["Beneficiary Name"]}}]}]
        }

    df = pd.read_csv(input_path)
    json_output = [validate_and_generate_json(row, idx + 1) for idx, row in df.iterrows() if row is not None]
    json_output = [entry for entry in json_output if entry]

    with open(output_path, 'w') as outfile:
        json.dump(json_output, outfile, indent=4)
    