"""
decide the user will purcase, income, age, education"""

import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X=np.array([[20,10000,12],[25,25000,3],[30,50000,5],[50,150000,5],[55,200000,6]])
y=np.array([1,1,0,1,0])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model=DecisionTreeClassifier()
result=model.fit(X_train, y_train)
user_pred=model.predict(X_test)
acc=accuracy_score(y_test, user_pred)
# print(acc)
input_data=np.array([[20,200000,12]])
results=model.predict(input_data)
if(results[0]==1):
  print("Customer will purchase")
else:
  print("Customer will not purchase")

