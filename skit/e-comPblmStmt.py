# """for e-com predict the user will purchase the high value product based on the age , time spent on website and the product is added on cart with logistic regression (supervised learning)"""

# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# "params as age, time spent, added to cart"
# X=np.array([[25,2,0], [30,3,1],[32,4,0],[45,1,1],[19,5,0],[28,6,1],[29,2,1]]) # feature matrix with sample
# # y=np.array([0,1,0,1,1])
# y=np.array(X[:, 2]) #extracting the add to cart from each sample
# # print(y)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# model=LogisticRegression()
# model.fit(X_train, y_train)
# 'checking the accuracy of the model'
# acc=model.score(X_test,y_test)
# print(f"{acc}")
# user_age=float(input("Enter the age: "))
# user_time=float(input("Enter the time spent: "))
# user_added=int(input("Did you added to cart o-no, 1-yes: "))
# print([user_added,user_time,user_added])
# input_data=np.array([[user_age, user_time,user_added]])
# result= model.predict(input_data)
# if(result[0]==1):
#   print("Yes high chances of buying")
# else:
#   print("No it will not buy")