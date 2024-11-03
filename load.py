import pandas as pd
import os

# Load the dataset
extraction_path = r'C:\Users\godre\Downloads\archive'
df = pd.read_csv(os.path.join(extraction_path, 'car data.csv'))

# Preview the data
print("Loaded Data:")
print(df.head())
