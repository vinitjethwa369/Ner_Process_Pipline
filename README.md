
# NER Model Training Pipeline

This repository provides a pipeline to preprocess data, annotate it, train a Named Entity Recognition (NER) model, and test it on new data. The pipeline is modular, and each step can be executed individually or as a complete flow.

---

## Folder Structure

```
project/
├── data/                  # Stores all data files
│   ├── input_data.csv     # Raw input data (to be provided by the user)
│   ├── cleaned_data.csv   # Cleaned and preprocessed data
│   ├── sampled_data.csv   # Sampled data
│   ├── shuffled_data.csv  # Shuffled data for annotation
│   ├── test_data.csv      # Test data for evaluation
├── models/                # Contains trained models
│   ├── ner_model/         # Trained spaCy model
│   └── ner_model.joblib   # Trained model in joblib format
├── output/                # Contains outputs generated during the pipeline
│   ├── training_data.json # JSON file for model training
│   ├── predicted_entities.csv # Model predictions
├── scripts/               # Python scripts for each pipeline stage
│   ├── preprocess.py      # Preprocessing and cleaning
│   ├── sample_shuffle.py  # Sampling and shuffling
│   ├── json_converter.py  # Convert CSV to JSON
│   ├── train_model.py     # Train the NER model
│   └── test_model.py      # Test the trained model
└── main.py                # Main script to run the full pipeline
```

---

## Prerequisites

Ensure Python is installed (>=3.8). Install the required packages using the following command:

```bash
pip install -r requirements.txt
```

### `requirements.txt` Content

```
pandas
scikit-learn
spacy
joblib
```

---

## Steps to Run the Pipeline

### 1. Clone the Repository

```bash
git clone <repository-url>
cd project
```

### 2. Place Raw Input Data

Put your raw input file in `data/input_data.csv`. Ensure the file contains a `Description` column.

---

### Running Each Step

#### **Step 1: Preprocess Data**

Run preprocessing to clean the raw input data:

```bash
python scripts/preprocess.py
```

Generates: `data/cleaned_data.csv`

---

#### **Step 2: Sample and Shuffle**

Run sampling and shuffling to prepare data for annotation:

```bash
python scripts/sample_shuffle.py
```

Generates: `data/sample_data.csv` and `data/shuffled_data.csv`

---

#### **Step 3: Convert CSV to JSON**

Convert the shuffled CSV to a training-ready JSON format:

```bash
python scripts/json_converter.py
```

Generates: `output/training_data.json`

---

#### **Step 4: Train the Model**

Train the NER model using the generated JSON file:

```bash
python scripts/train_model.py
```

Generates: `models/ner_model`

---

#### **Step 5: Test the Model**

Test the model on new data (`data/test_data.csv`):

```bash
python scripts/test_model.py
```

Generates: `output/predicted_entities.csv`

---

### Running the Full Pipeline

Run all steps sequentially with a single command:

```bash
python main.py
```

Outputs will be saved in the respective folders.

---

## Outputs

- **Preprocessed Data:** `data/cleaned_data.csv`
- **Sampled Data:** `data/sampled_data.csv`
- **Shuffled Data:** `data/shuffled_data.csv`
- **Training JSON:** `output/training_data.json`
- **Trained Model:** `models/ner_model` and `models/ner_model.joblib`
- **Predictions:** `output/predicted_entities.csv`

---

## License

This project is licensed under the MIT License.

---

## Contributions

Feel free to open issues or submit pull requests for improvements.
