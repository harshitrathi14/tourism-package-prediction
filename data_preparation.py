import pandas as pd
import os
from sklearn.model_selection import train_test_split

def prepare_data():
    print("Starting Data Preparation...")
    file_path = 'data/tourism.csv'
    df = pd.read_csv(file_path)
    
    # Drop unnecessary columns
    cols_to_drop = ['CustomerID']
    if 'Unnamed: 0' in df.columns:
        cols_to_drop.append('Unnamed: 0')
    
    df = df.drop(columns=[col for col in cols_to_drop if col in df.columns])
    print(f"Dropped columns: {cols_to_drop}")
    
    # Handle Gender inconsistencies
    if 'Gender' in df.columns:
        df['Gender'] = df['Gender'].replace('Fe Male', 'Female')
    
    print("Data cleaning complete.")
    
    # Separate target and features for splitting (to stratify)
    X = df.drop(columns=['ProdTaken'])
    y = df['ProdTaken']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # Combine features and target for saving
    train_data = pd.concat([X_train, y_train], axis=1)
    test_data = pd.concat([X_test, y_test], axis=1)
    
    # Save datasets locally
    train_data.to_csv('data/train_data.csv', index=False)
    test_data.to_csv('data/test_data.csv', index=False)
    
    print(f"Train and test datasets saved to 'data/'. Train shape: {train_data.shape}, Test shape: {test_data.shape}")
    print("Data Preparation Complete.")

if __name__ == '__main__':
    prepare_data()
