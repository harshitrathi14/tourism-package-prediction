import pandas as pd
import json
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, classification_report
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

def build_model():
    print("Starting Model Building...")
    train_df = pd.read_csv('data/train_data.csv')
    test_df = pd.read_csv('data/test_data.csv')
    
    X_train = train_df.drop(columns=['ProdTaken'])
    y_train = train_df['ProdTaken']
    
    X_test = test_df.drop(columns=['ProdTaken'])
    y_test = test_df['ProdTaken']
    
    numeric_features = X_train.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = X_train.select_dtypes(include=['object']).columns

    numeric_transformer = SimpleImputer(strategy='median')
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    rf = RandomForestClassifier(random_state=42)
    
    clf = Pipeline(steps=[('preprocessor', preprocessor),
                          ('classifier', rf)])

    param_grid = {
        'classifier__n_estimators': [50, 100],
        'classifier__max_depth': [10, 20, None]
    }
    
    print("Tuning hyperparameters using GridSearchCV...")
    grid_search = GridSearchCV(clf, param_grid, cv=3, n_jobs=-1, scoring='accuracy')
    grid_search.fit(X_train, y_train)
    
    best_model = grid_search.best_estimator_
    best_params = grid_search.best_params_
    
    print(f"Best Parameters: {best_params}")
    
    with open('best_params.json', 'w') as f:
        json.dump(best_params, f)
        
    print("Evaluating model performance on test set...")
    y_pred = best_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Model Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    joblib.dump(best_model, 'model.pkl')
    print("Best model (pipeline) saved to 'model.pkl'.")
    print("Model Building Complete.")

if __name__ == '__main__':
    build_model()
