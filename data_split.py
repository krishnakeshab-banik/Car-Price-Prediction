import pandas as pd
from sklearn.model_selection import train_test_split

# Load the cleaned data
df = pd.read_csv('cleaned_car_data.csv')

# Split the dataset into features and target variable
X = df.drop('Selling_Price', axis=1)  # Features
y = df['Selling_Price']                # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save the split data
X_train.to_csv('X_train.csv', index=False)
X_test.to_csv('X_test.csv', index=False)
y_train.to_csv('y_train.csv', index=False)
y_test.to_csv('y_test.csv', index=False)

print("Data split and saved.")
