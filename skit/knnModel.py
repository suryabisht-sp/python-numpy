"""Powerful K-Nearest Neighbors (KNN) Model age, salary, purchase history, satisfaction """

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler # 
from sklearn.neighbors import KNeighborsClassifier

data =np.array([[25,25000,1],[30,60000,2],[20,30000,1],[40,95000,1],[45,80000,2],[65,95000,2]])
# print(data)
labels=np.array([1,2,0,1,2,2]) #0:low, 1:medium, 2:high
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=.2, random_state=0)
"""normalise it before using it"""
scaler=StandardScaler()
"fit transfrom that 80% and save it again on x train"
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)

"number of neightbors will be 3"
model=KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
acc=model.score(X_test,y_test)
# print(f"{acc}")50
# user_age=float(input("Enter age: "))
# user_sal=int(input("Enter salary: "))
# user_prof=int(input("Enter past history: "))
# input_data=np.array([[user_age,user_sal, user_prof]])
input_data=np.array([[25,50000,1]])
scalerd=scaler.transform(input_data)
result=model.predict(scalerd)
# print(result)
