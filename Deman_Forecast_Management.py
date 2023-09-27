# Import the necessary libraries
import pandas as pd  # For data handling
import numpy as np   # For numerical operations
import matplotlib.pyplot as plt  # For plotting
from sklearn.model_selection import train_test_split  # For splitting data
from sklearn.ensemble import RandomForestRegressor  # For the machine learning model
from sklearn.metrics import mean_squared_error  # For evaluating model performance

# Load your dataset (replace 'your_dataset.csv' with your actual dataset file)
data = pd.read_csv('your_dataset.csv')

# Ensure that the 'Date' column is in a datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Set the 'Date' column as the index of the dataset
data.set_index('Date', inplace=True)

# Add some additional features (you can add more as needed)
data['Year'] = data.index.year
data['Month'] = data.index.month
data['Day'] = data.index.day
data['DayOfWeek'] = data.index.dayofweek

# Split the data into training and testing sets (80% for training, 20% for testing)
train_size = int(len(data) * 0.8)
train_data, test_data = data[:train_size], data[train_size:]

# Define the features (X) and the target variable (y) for training and testing
X_train = train_data.drop('Demand', axis=1)
y_train = train_data['Demand']
X_test = test_data.drop('Demand', axis=1)
y_test = test_data['Demand']

# Create and train the machine learning model (Random Forest in this example)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions using the trained model
y_pred = model.predict(X_test)

# Evaluate the model's performance using Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Visualize the actual demand vs. predicted demand (optional)
plt.figure(figsize=(12, 6))
plt.plot(test_data.index, y_test, label='Actual Demand')
plt.plot(test_data.index, y_pred, label='Predicted Demand', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Demand')
plt.legend()
plt.show()

# You can save the trained model for future demand forecasting
# joblib.dump(model, 'demand_forecasting_model.joblib')

