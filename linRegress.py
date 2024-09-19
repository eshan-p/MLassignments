# Name:     Eshan Patel
# NetID:    exp200016
# Section:  4375.001

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
  
# pulling dataset on github repo
url = 'https://raw.githubusercontent.com/eshan-p/LinRegGD-Wine-Data/main/winequality-red.csv'
dataset = pd.read_csv(url, sep=';', on_bad_lines='skip')

# seperating features (X) from target (Y)
X = dataset.drop('Quality', axis=1)
Y = dataset['Quality']

# split data into training and test sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
 
# standardizing features of both training and test sets
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# hyperparameters
maxIter = 25000
eta0Val = 0.0035
alpha = 0.0025

model = SGDRegressor(alpha=alpha, max_iter=maxIter, learning_rate='constant', eta0=eta0Val)
model.fit(X_train_scaled, Y_train)

Y_train_pred = model.predict(X_train_scaled)
Y_test_pred = model.predict(X_test_scaled)

# calculate MSE for current trial
trainError = mean_squared_error(Y_train, Y_train_pred)
testError = mean_squared_error(Y_test, Y_test_pred)

# calculate r^2 values for current trial
trainR2 = r2_score(Y_train, Y_train_pred)
testR2 = r2_score(Y_test, Y_test_pred)

# printing info to terminal 
print(f"Num of iterations: {maxIter}, initial learning rate: {eta0Val}, alpha: {alpha}")
print(f"Training Error: {trainError}, Training r2: {trainR2}, Test Error: {testError}, Test r2: {testR2}")

# printing info to log file
logFile = open("GDlogfile.txt", "a")
logFile.write(f"Num of iterations: {maxIter}, initial learning rate: {eta0Val}, alpha: {alpha}\n")
logFile.write(f"Training Error: {trainError}, Training r2: {trainR2}, Test Error: {testError}, Test r2: {testR2}\n\n")
logFile.close()

# importance of features plot
'''
feat_importance = model.coef_
plt.figure(figsize=(10, 6))
plt.barh(X.columns, feat_importance)
plt.title("Importance of Features")
plt.xlabel("Coefficient value")
plt.ylabel("Feature")
plt.show()
'''

# distribution of residuals (histogram)
'''
residuals = Y_test_pred - Y_test
plt.figure(figsize=(10, 6))
sns.histplot(residuals)
plt.title('Distribution of Residuals')
plt.xlabel('Residuals')
plt.show()
'''