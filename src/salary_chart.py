# Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv('../dat/Salary_dataset.csv')

# Extracting the features and target variable
X = data[['YearsExperience']]
y = data['Salary']

# Create and train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Predictions using the model
predicted_salary = model.predict(X)

# Plotting the data points
plt.scatter(X, y, color='blue', label='Actual Salary')

# Plotting the regression line
plt.plot(X, predicted_salary, color='red', label='Regression Line')

# Chart Details
plt.title('Years of Experience vs. Salary')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.grid(True)
plt.show()
