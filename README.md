The project entails developing a machine learning model that would predict the selling price of cars given multiple features. The steps that follow represent the workflow for the project:

1. Data Collection

- For this project, the data is taken from [Kaggle](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho).
- The dataset has all features like car name, year of manufacturing, price selling, present price, kilometers driven, fuel type, seller type, transmission type, and number of owners.
 
2. Data Extraction
- Extracted the dataset as a ZIP file and copied that to a local directory to make the analysis.
- The main CSV file has been loaded for analysis into the application, `car data.csv`.

3. Data Cleaning and Preparation
The data cleaning starts by analyzing the missing values and the type of data.
 Irrelevant columns are deleted for reduction of data
 One-hot encoding of categorical variables such as fuel type, seller type, and transmission have been done and are transformed into a numerical format to enable training in the model.
- Data is divided into training and testing sets, where 80% of the data is used for training and 20% for testing.

5. Training Model
- The chosen machine learning model for this project is a Random Forest Regressor.
- The model is trained on the training dataset.

6. Model Evaluation
- The trained model is evaluated on the test dataset.
- Key evaluation metrics are calculated, such as
- Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)
  - R-squared (R²)

Explanation of Each Section

- Data Collection: Gives the source of the data set and what it actually contains.
- Data Extraction: What the dataset is extracted from the zip file
- Data Cleaning and Preparation: Defines the cleaning process and transforms categorical data.
- Data Splitting: How the data is prepared for training and testing.
- Model Training: The model applied and the training process.
- Model Evaluation: The metrics used to measure the performance of the model.
- Future Improvements: Areas where the model can be further developed.

Modules to be downloaded-
1.Panda
2.scikit-learn
