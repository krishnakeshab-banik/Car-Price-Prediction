import pandas as pd
import os

# Load the dataset
extraction_path = r'C:\Users\godre\Downloads\archive'  
df = pd.read_csv(os.path.join(extraction_path, 'car data.csv'))

# Checking for missing values and data types
print("Missing values in each column:")
print(df.isnull().sum())
print("\nData Types:")
print(df.dtypes)

# Drops unnecessary columns
df.drop(['Car_Name'], axis=1, inplace=True)

df = pd.get_dummies(df, columns=['Fuel_Type', 'Seller_Type', 'Transmission'], drop_first=True)
df.to_csv('cleaned_car_data.csv', index=False)
print("Data cleaned and saved.")
