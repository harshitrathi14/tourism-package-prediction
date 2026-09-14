import pandas as pd
import os
import sys

def register_data(file_path):
    print("Starting Data Registration...")
    if not os.path.exists(file_path):
        print(f"Error: Dataset not found at {file_path}")
        sys.exit(1)
        
    df = pd.read_csv(file_path)
    
    expected_columns = [
        'CustomerID', 'ProdTaken', 'Age', 'TypeofContact', 'CityTier',
        'DurationOfPitch', 'Occupation', 'Gender', 'NumberOfPersonVisiting',
        'NumberOfFollowups', 'ProductPitched', 'PreferredPropertyStar',
        'MaritalStatus', 'NumberOfTrips', 'Passport', 'PitchSatisfactionScore',
        'OwnCar', 'NumberOfChildrenVisiting', 'Designation', 'MonthlyIncome'
    ]
    
    missing_cols = [col for col in expected_columns if col not in df.columns]
    
    if missing_cols:
        print(f"Error: Missing expected columns: {missing_cols}")
        sys.exit(1)
        
    print("Dataset Validation Successful. All expected columns are present.")
    print("\nDataset Summary:")
    print(f"Total Rows: {len(df)}")
    print(f"Total Columns: {len(df.columns)}")
    print("\nColumn Data Types:")
    print(df.dtypes)
    print("\nData Registration Complete.")

if __name__ == '__main__':
    data_path = 'data/tourism.csv'
    register_data(data_path)
