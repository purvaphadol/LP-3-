# -*- coding: utf-8 -*-
"""pract2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11kFXGiaYIKIYBN72hcWCcFy7cd-jQ7Bj
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
#from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix, accuracy_score, precision_score, recall_score, plot_precision_recall_curve, plot_roc_curve
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

df = pd.read_csv('emails.csv')

print(df.isnull().sum())

df.head()

df.tail()

x=df.iloc[:,1:-1].values
y=df.iloc[:,-1].values

# x will contain columns from index 1 to 3000, for a total of 3000 columns.
# y will contain the values in column 3001.

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=10)

kNN = KNeighborsClassifier(n_neighbors=10)
kNN.fit(x_train, y_train)
print("K-Nearest Neighbors Performance:")

y_pred = kNN.predict(x_test)

from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
cm = confusion_matrix(y_test, y_pred)
print(cm)

from sklearn.metrics import ConfusionMatrixDisplay
display = ConfusionMatrixDisplay(cm)
display.plot()

accuracy_score(y_test, y_pred)

precision_score(y_test, y_pred)

recall_score(y_test, y_pred)

from sklearn.metrics import plot_precision_recall_curve, plot_roc_curve

# Assuming `kNN` is a trained model, and `x_test`, `y_test` are your test data
plot_precision_recall_curve(kNN, x_test, y_test)
plot_roc_curve(kNN, x_test, y_test)

plot_roc_curve(kNN, x_test, y_test)

svm = SVC(gamma='auto', random_state=10)
svm.fit(x_train, y_train)

y_pred = svm.predict(x_test)

accuracy_score(y_test, y_pred)

