# Tourism Package Prediction

This project builds an MLOps workflow for predicting whether a customer is likely to purchase the Wellness Tourism Package.

## Project Links

- GitHub repository: https://github.com/harshitrathi14/tourism-package-prediction
- Streamlit app: https://tourism-package-prediction-zrgfbaar4vmzucwyzawe7x.streamlit.app/

## Repository Structure

```text
.
├── .github/workflows/pipeline.yml
├── data/
│   ├── tourism.csv
│   ├── train_data.csv
│   └── test_data.csv
├── app.py
├── data_registration.py
├── data_preparation.py
├── model_building.py
├── model.pkl
├── best_params.json
├── requirements.txt
└── README.md
```

## Workflow

1. `data_registration.py` validates that the source dataset has the expected columns and prints a dataset summary.
2. `data_preparation.py` cleans the dataset, removes unnecessary columns, fixes inconsistent gender labels, and creates train/test splits.
3. `model_building.py` trains a Random Forest pipeline with preprocessing, tunes hyperparameters with GridSearchCV, evaluates the model, and saves the best model.
4. `.github/workflows/pipeline.yml` automates the registration, preparation, model training, and model artifact update steps through GitHub Actions. The workflow uploads the prepared train/test CSV files as an artifact and downloads them in the model-building job.
5. `app.py` serves the trained model through Streamlit for customer-level purchase prediction.

## Model Summary

- Algorithm: Random Forest Classifier
- Best parameters: `classifier__max_depth=20`, `classifier__n_estimators=100`
- Test accuracy: `0.9128`

## Deployment

The Streamlit app loads `model.pkl`, collects customer and interaction details, and returns whether the customer is likely to purchase the Wellness Tourism Package.
