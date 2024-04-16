# """tel com want to reduce customer churn by identifying the customer at risk of leaving"""
# """taking recharge, age, likely to buy or not"""

# import numpy as np
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.svm import SVC
# from sklearn.metrics import accuracy_score, classification_report # checking the score and report to evaluate the performance of modal
# data={"age":[18,22,24,58], "rec":[250,250,150,150,],"purchase":[1,1,0,0]}
# df=pd.DataFrame(data)
# X=df[["age", "rec"]]
# y=df["purchase"]

# X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=.2, random_state=42)

# 'svc= support vector classifier, kernal are the method inside svc, c is default regularisation'
# model=SVC(kernel="linear", C=1.0)
# model.fit(X_train,y_train)
# # result=model.predict(X_test)
# # acc=accuracy_score(y_test,result)
# # repo=classification_report(y_test, result)
# # print(repo)
# user_age=float(input("Enter the age: "))
# user_rech=float(input("Enter the recharge: "))
# print([user_age,user_rech])
# input_data=np.array([[user_age, user_rech]])
# prd=model.predict(input_data)
# # print(prd)17

# if(prd[0]==0):
#   print("Customer will do recharge")
# else:
#   print("Customer will leave")
