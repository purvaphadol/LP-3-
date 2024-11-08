# -*- coding: utf-8 -*-
"""pract1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iuT92C5jRZfANUu_PHEciuqnCyy4OqG7

Predict the price of the Uber ride from a given pickup point to the agreed drop-off location.
Perform following tasks:
1. Pre-process the dataset.
2. Identify outliers.
3. Check the correlation.
4. Implement linear regression and random forest regression models.
5. Evaluate the models and compare their respective scores like R2, RMSE, etc.
Dataset link: https://www.kaggle.com/datasets/yasserh/uber-fares-dataset
"""

import pandas as pd
import numpy as np
import seaborn as sns

#from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix, accuracy_score, precision_score, recall_score
# , plot_precision_recall_curve, plot_roc_curve

df=pd.read_csv('./uber.csv')

df.isnull().sum()

df['dropoff_longitude'].fillna(df['dropoff_longitude'].mean(),inplace=True)
df['dropoff_latitude'].fillna(df['dropoff_latitude'].mean(),inplace=True)

df.drop(labels='Unnamed: 0',axis=1,inplace=True)
df.drop(labels='key',axis=1,inplace=True)

df.isnull().sum()

df.dtypes

sns.boxplot(x= df['dropoff_latitude'])

sns.boxplot(x=df['fare_amount'])

def find_outliers_IQR(df):
   q1 = df.quantile(0.25)
   q3 = df.quantile(0.75)
   IQR = q3-q1
   outliers = df[((df<(q1-1.5*IQR)) | (df>(q3+1.5*IQR)))]
   return outliers

outliers = find_outliers_IQR(df["fare_amount"])
print("number of outliers: "+ str(len(outliers)))
print("max outlier value: "+ str(outliers.max()))
print("min outlier value: "+ str(outliers.min()))
outliers

outliers = find_outliers_IQR(df["pickup_latitude"])
print("number of outliers: "+ str(len(outliers)))
print("max outlier value: "+ str(outliers.max()))
print("min outlier value: "+ str(outliers.min()))
outliers

df = df[
    (df.pickup_latitude > -90) & (df.pickup_latitude < 90) &
    (df.dropoff_latitude > -90) & (df.dropoff_latitude < 90) &
    (df.pickup_longitude > -180) & (df.pickup_longitude < 180) &
    (df.dropoff_longitude > -180) & (df.dropoff_longitude < 180) &
    (df.fare_amount > 0) &
    (df.passenger_count > 0) & (df.passenger_count < 50)
]

df.info

df.head()

def haversine(lat1,lon1,lat2,lon2):
    lat1,lon1,lat2,lon2=map(np.radians,[lat1,lon1,lat2,lon2])
    dlat=lat2-lat1
    dlon=lon2-lon1
    a = np.sin(dlat / 2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2)**2
    c=2*np.arcsin(np.sqrt(a))
    return 6371 * c
df['distance']=haversine(df['pickup_latitude'],df['pickup_longitude'],df['dropoff_latitude'],df['dropoff_longitude'])

df['distance']=haversine(df['pickup_latitude'],df['pickup_longitude'],df['dropoff_latitude'],df['dropoff_longitude'])

df.head()

df.head()

sns.boxplot(x= df['distance'])

df = df[(df['distance'] > 0) & (df['distance'] < 200)]
sns.boxplot(x=df['distance'])

df.drop(columns=['pickup_datetime', 'pickup_latitude', 'pickup_longitude', 'dropoff_latitude', 'dropoff_longitude'], inplace=True)

print("\nCorrelation Matrix:")
print(df.corr())

# Visualize the relationship between 'Distance' and 'fare_amount'
sns.scatterplot(x='distance', y='fare_amount', data=df)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

X = df[['distance']]
y = df['fare_amount']

# Splitting dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling the data
scaler_X = StandardScaler()
scaler_y = StandardScaler()

X_train = scaler_X.fit_transform(X_train)
X_test = scaler_X.transform(X_test)

model=LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Calculate Mean Absolute Error (MAE)
mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error (MAE):", mae)

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error (MSE):", mse)

# Calculate Root Mean Squared Error (RMSE)
rmse = mean_squared_error(y_test, y_pred, squared=False)
print("Root Mean Squared Error (RMSE):", rmse)

# Calculate R-squared (R²)
r2 = r2_score(y_test, y_pred)
print("R-squared (R²):", r2)

model_r=RandomForestRegressor(n_estimators=100, random_state=42)

model_r.fit(X_train, y_train)

y_pred_3 = model_r.predict(X_test)

r_squared = r2_score(y_test, y_pred_3)
print(r_squared)

rmse = mean_squared_error(y_test, y_pred_3, squared=False)
mae = mean_absolute_error(y_test, y_pred_3)
print(rmse)
print(mae)

# Example distance value (in kilometers) for prediction
input_distance = 10.0  # Replace this with the distance you want to predict for

# 1. Prepare the input for prediction
# Create a DataFrame with the distance value
input_data = pd.DataFrame({'distance': [input_distance]})

# 2. Scale the input data using the previously fitted scaler
scaled_input = scaler_X.transform(input_data)

# 3. Make predictions using both models
predicted_fare_lr = model.predict(scaled_input)
predicted_fare_rf = model_r.predict(scaled_input)

# 4. Output the predicted fare
print(f"Predicted fare using Linear Regression for {input_distance} km: ${predicted_fare_lr[0]:.2f}")
print(predicted_fare_lr)
print(f"Predicted fare using Random Forest Regression for {input_distance} km: ${predicted_fare_rf[0]:.2f}")

