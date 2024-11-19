import spacy
import pandas as pd
import os

def test_model(model_path, test_data_path, output_path):
    print("Testing the model...")

    nlp = spacy.load(model_path)
    test_data = pd.read_csv(test_data_path)
    results = []

    for text in test_data['Description'].astype(str).fillna('').tolist():
        if text.strip():
            doc = nlp(text)
            entities = ", ".join([f"{ent.text}" for ent in doc.ents]) if doc.ents else "No entity"
            results.append({"Description": text, "Entity": entities})
        else:
            results.append({"Description": text, "Entity": "No text found"})

    output_df = pd.DataFrame(results)
    output_df.to_csv(output_path, index=False)
    print(f"Predicted entities saved to {output_path}")

if __name__ == "__main__":
    os.makedirs("output", exist_ok=True)
    test_model("models/ner_model", "data/test_data.csv", "output/predicted_entities.csv")
