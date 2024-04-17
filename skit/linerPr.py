# """
# predict student result using linear regression model
# """
# import numpy as np
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# """'why linear as the data is linear'"""
# datal = {"Hours": [1, 2, 3, 4, 5, 6, 7, 8], "scores": [50, 60, 65, 70, 50, 90, 80, 85]}
# tdata = pd.DataFrame(datal)
# # print(tdata)
# """'extraction data from the table or column is feature extraction, xtrain xtest ytrain ytest'"""
# X = tdata[["Hours"]]  # Features
# y = tdata["scores"]   # Target variable
# # print(X)
# """test_size=0.2 represent the % for test .2 means 20%, random_state=42 means this much time the data will train"""
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# """instance of linear regression model"""
# model=LinearRegression()
# # print(model.fit(X_train, y_train))
# model.fit(X_train, y_train)

# """user input data"""
# user_input=float(input("Enter the hours: "))
# # user_hours=float(input("Enter the hours: "))
# """providing the user input to model for prediction"""
# result=model.predict([[user_input]])
# # print(f"Predicted score for the enter time is {result[0]:.2f} ")