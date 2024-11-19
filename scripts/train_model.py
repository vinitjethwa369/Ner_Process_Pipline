import spacy
from spacy.training import Example
import json
import os

def train_model(json_path, model_output_dir):
    print("Starting model training...")

    with open(json_path, 'r') as file:
        training_data = json.load(file)

    TRAINING_DATA = []
    for item in training_data:
        text = item['data']['text']
        entities = []
        for annotation in item.get('annotations', []):
            for result in annotation.get('result', []):
                value = result.get('value', {})
                if 'start' in value and 'end' in value and 'labels' in value:
                    entities.append((value['start'], value['end'], value['labels'][0]))
        TRAINING_DATA.append((text, {"entities": entities}))

    # Train spaCy model
    nlp = spacy.blank("en")
    if "ner" not in nlp.pipe_names:
        ner = nlp.add_pipe("ner")
    else:
        ner = nlp.get_pipe("ner")

    for _, annotations in TRAINING_DATA:
        for ent in annotations['entities']:
            ner.add_label(ent[2])

    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
    with nlp.disable_pipes(*other_pipes):
        optimizer = nlp.begin_training()
        for iteration in range(30):
            print(f"Iteration {iteration + 1}...")
            losses = {}
            for text, annotations in TRAINING_DATA:
                example = Example.from_dict(nlp.make_doc(text), annotations)
                nlp.update([example], drop=0.3, losses=losses)
            print(f"Losses at iteration {iteration + 1}: {losses}")

    nlp.to_disk(model_output_dir)
    print(f"Model saved to {model_output_dir}")

if __name__ == "__main__":
    os.makedirs("models", exist_ok=True)
    train_model("output/training_data.json", "models/ner_model")
