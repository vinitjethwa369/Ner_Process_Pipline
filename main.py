import os
from scripts.preprocess import preprocess_data
from scripts.sample_shuffle import sample_data, shuffle_data
from scripts.json_converter import prepare_json
from scripts.train_model import train_model
from scripts.test_model import test_model

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    os.makedirs("models", exist_ok=True)

    # # Step 1: Preprocess data
    # preprocess_data("data/input_data.csv", "data/cleaned_data.csv")

    # Step 2: Sample and shuffle
    sample_data("data/cleaned_data.csv", "data/sampled_data.csv")
    shuffle_data("data/sampled_data.csv", "data/shuffled_data.csv")

    # Step 3: Prepare JSON
    prepare_json("data/shuffled_data.csv", "output/training_data.json")

    # Step 4: Train the model
    train_model("output/training_data.json", "models/ner_model")

    # Step 5: Test the model
    test_model("models/ner_model", "data/test_data.csv", "output/predicted_entities.csv")
