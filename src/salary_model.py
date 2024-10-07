# Required Libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load the dataset
data = pd.read_csv('../dat/Salary_dataset.csv')

# Extracting the features and target variable
X = data[['YearsExperience']]
y = data['Salary']

# Create and train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Save the model to a file
joblib.dump(model, '../model/Salary_model.pkl')

print("Model has been saved as 'Salary_model.pkl'.")