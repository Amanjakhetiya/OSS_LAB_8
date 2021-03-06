# -*- coding: utf-8 -*-
"""Amanjakhetiya_9918103209_F8_OSS_LAB8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FdyA0RAYk5fVVsvtEmPwdFuI0xl4R8Nt
"""

# Q1.

import numpy as np
from scipy import sparse
eye = np.eye(4)
print("NumPy array:\n", eye)
sparse_matrix = sparse.csr_matrix(eye)
print("\nSciPy sparse matrix in CSR format:\n", sparse_matrix)

# Q2.
from google.colab import files
files.upload()

import pandas as pd
df = pd.read_csv("Iris (2).csv")
df.describe()

df

# Q3.
import pandas as pd
from sklearn.model_selection import train_test_split

df.drop('Id',axis=1,inplace=True)

y= df['Species']
X=df.drop('Species',axis=1)

X.shape,y.shape

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

print("\n70% train data:")
print(X_train)
print(y_train)
print("\n30% test data:")
print(X_test)
print(y_test)

# Q4.

new_X_train,new_X_test,new_Y_train,new_Y_test=train_test_split(X,y,test_size=0.20)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

neigh =KNeighborsClassifier(n_neighbors=3)
neigh.fit(new_X_train, new_Y_train)
pred = neigh.predict(new_X_test)
print ("KNeighbors accuracy score :",accuracy_score(new_Y_test,
pred))

# Q5.

from sklearn.datasets import load_boston
boston_dataset = load_boston() 
boston_dataset

X,y=boston_dataset['data'],boston_dataset['target']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =train_test_split(X,y,random_state=0)

from sklearn.linear_model import LinearRegression
reg = LinearRegression().fit(X_train, y_train)

from sklearn.metrics import mean_absolute_error
pred=reg.predict(X_test)
print(mean_absolute_error(pred,y_test))

