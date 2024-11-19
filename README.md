
# NER Pipeline

This repository contains a Named Entity Recognition (NER) pipeline that processes financial transaction data, trains an NER model using spaCy, and tests the model for entity recognition.

---

## Project Structure

```
ner_pipeline/
├── data/
│   ├── Training_data.csv         # Raw training data
│   ├── Testing_data.csv          # Test data
│   ├── cleaned_data.csv          # Preprocessed cleaned data
│   ├── sampled_data.csv          # Sampled training data
│   ├── shuffled_data.csv         # Shuffled training data
│   ├── Training_Json_Data.json   # JSON data for training
│   ├── Predicted_entities.csv    # Output from model testing
├── models/
│   ├── Trained_NER_Model/        # Saved trained model
│   ├── NER_Model.joblib          # Serialized model
├── scripts/
│   ├── __init__.py
│   ├── preprocess.py             # Preprocessing logic
│   ├── generate_json.py          # Generate JSON for training
│   ├── train_model.py            # Model training logic
│   ├── test_model.py             # Model testing logic
├── main.py                       # Main script to run the pipeline
└── README.md                     # Instructions and usage
```

---

## Setup Instructions

### 1. Clone the Repository
Clone this repository and navigate to the `ner_pipeline` folder:
```bash
git clone <repository-url>
cd ner_pipeline
```

### 2. Create a Virtual Environment
Create and activate a virtual environment:
```bash
python -m venv ner_env
source ner_env/bin/activate  # On macOS/Linux
ner_env\Scripts\activate     # On Windows
```

### 3. Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

---

## Pipeline Workflow

### 1. Preprocessing
Preprocess the raw training data to clean and normalize it:
```bash
python scripts/preprocess.py
```

### 2. Generate JSON Data
Convert the cleaned data into a JSON format suitable for spaCy model training:
```bash
python scripts/generate_json.py
```

### 3. Train the NER Model
Train the spaCy NER model using the JSON training data:
```bash
python scripts/train_model.py
```

### 4. Test the Model
Test the trained model on unseen data and save the predictions:
```bash
python scripts/test_model.py
```

### 5. Run the Entire Pipeline
Execute all the steps from preprocessing to testing in sequence:
```bash
python main.py
```

---

## Bash Shortcuts

- **Activate Virtual Environment**:
  ```bash
  source ner_env/bin/activate  # On macOS/Linux
  ner_env\Scripts\activate     # On Windows
  ```

- **Deactivate Virtual Environment**:
  ```bash
  deactivate
  ```

- **Install New Dependencies**:
  If you need to add new Python packages, install them and update the `requirements.txt` file:
  ```bash
  pip install <package-name>
  pip freeze > requirements.txt
  ```

---

## File Descriptions

- **`data/`**: Contains raw, intermediate, and final data files used in the pipeline.
- **`models/`**: Stores the trained model and serialized model file for deployment or reuse.
- **`scripts/`**: Contains Python scripts for different steps in the pipeline:
  - `preprocess.py`: Handles data cleaning and preprocessing.
  - `generate_json.py`: Converts cleaned data into JSON format for spaCy training.
  - `train_model.py`: Defines and trains the spaCy NER model.
  - `test_model.py`: Tests the trained model and saves the predictions.
- **`main.py`**: Orchestrates the entire pipeline in a single run.
- **`README.md`**: Provides project documentation and usage instructions.

---

## Requirements

The project uses the following Python libraries:
- `pandas==1.3.5`
- `matplotlib==3.5.1`
- `spacy==3.5.0`
- `joblib==1.3.2`
- `scikit-learn==1.0.2`
- `numpy==1.21.6`

To install all dependencies:
```bash
pip install -r requirements.txt
```

---

## How It Works

1. **Preprocessing**: Cleans transaction descriptions, removes special characters, and extracts meaningful components for training.
2. **JSON Conversion**: Converts cleaned data into a spaCy-compatible JSON structure for training the NER model.
3. **Training**: Trains a spaCy model to recognize entities in transaction descriptions.
4. **Testing**: Tests the trained model on unseen data and saves entity predictions.

---

## Outputs

- **`cleaned_data.csv`**: Preprocessed data ready for analysis.
- **`Training_Json_Data.json`**: JSON-formatted training data for spaCy.
- **`Trained_NER_Model/`**: Directory containing the trained spaCy model.
- **`NER_Model.joblib`**: Serialized model for future use.
- **`Predicted_entities.csv`**: Output file containing the model's predictions.

---

## Example Commands

Run preprocessing:
```bash
python scripts/preprocess.py
```

Run the full pipeline:
```bash
python main.py
```

---

## Contributing

Feel free to fork this repository and submit pull requests for improvements or bug fixes. Always work in a new branch and submit your PR to the `main` branch.

---

## License

This project is licensed under the [MIT License](LICENSE).
