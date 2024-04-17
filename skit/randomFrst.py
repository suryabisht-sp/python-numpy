# """
# Random Forest in Scikit-learn
# """
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score
# import pandas as pd
# "we can't process the alphabt so labelencoder is required"
# from sklearn.preprocessing import LabelEncoder

# data={"age":[20,25,30,35,40,45], "gender":["m","m","f","f","m","f"], "estimatedsalary":[25000,30000,35000,40000,50000,60000],"purchased":[1,1,1,0,1,1]}
# # print(data)
# df=pd.DataFrame(data)
# lebEncoder=LabelEncoder()
# df['gender']=lebEncoder.fit_transform(df['gender']) #male =1 , female=0
# # print(df)
# X=df.drop("purchased", axis=1)
# y=df["purchased"]
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# model=RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)
# pred=model.predict(X_test)
# acc=accuracy_score(y_test,pred)
# # print(acc)
# user_age=int(input("enter age: "))
# user_gender=(input("enter gender in small: "))
# user_salary=int(input("enter salary: "))
# user_gender_endcode=lebEncoder.transform([ user_gender ])[0]
# print(user_gender_endcode)
# user_input_data=[[user_age, user_gender_endcode, user_salary]]
# result= model.predict(user_input_data)
# print(result)
# # plsa75


