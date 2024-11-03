import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load the split data
X_train = pd.read_csv('X_train.csv')
y_train = pd.read_csv('y_train.csv').values.ravel()  # Flatten to 1D array

# Train the model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Save the trained model using joblib
import joblib
joblib.dump(model, 'random_forest_model.pkl')
print("Model trained and saved.")
