# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import GradientBoostingRegressor
# from sklearn.metrics import mean_squared_error
# import pandas as pd

# data = {'Square Feet': [1500, 2000, 1200, 1800, 1350],
#         'Bedrooms': [3, 4, 2, 3, 3],
#         'Bathrooms': [2, 2.5, 1.5, 2, 2],
#         'Location': ["Suburb", "City", "Rural", "City", "Suburb"],
#         'Prices': [250000, 300000, 180000, 280000, 220000]}

# df = pd.DataFrame(data)

# # Convert location into dummy variables
# df = pd.get_dummies(df, columns=["Location"])

# X = df.drop("Prices", axis=1)
# y = df["Prices"]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = GradientBoostingRegressor()
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)

# print("Mean Squared Error:", mse)

# print("Enter the Details one by one")
# sq_foot = float(input("Enter the Area you want in sqft: "))
# bedR = int(input("Enter the Bedrooms you want: "))
# bathR = float(input("Enter the Bathrooms you want: "))
# Locat = input("Enter the Location you want (Suburb, City, or Rural): ")

# input_locat = [0, 0, 0]
# if Locat == "Suburb":
#     input_locat[0] = 1
# elif Locat == "City":
#     input_locat[1] = 1
# elif Locat == "Rural":
#     input_locat[2] = 1

# user_input = pd.DataFrame({'Square Feet': [sq_foot],
#                            'Bedrooms': [bedR],
#                            'Bathrooms': [bathR],
#                            'Location_City': [input_locat[1]],
#                            'Location_Rural': [input_locat[2]],
#                            'Location_Suburb': [input_locat[0]]})

# print(user_input)

# prediction = model.predict(user_input)
# print("Price is:", prediction[0])
