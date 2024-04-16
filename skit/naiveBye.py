# """
# Creating Model with Naive Bayes, understandign the customer's satisfaction and sentiments, for positive its 1 negative it be 0
# """

# import numpy as np
# from sklearn.feature_extraction.text import CountVectorizer #will convert the text into metrix so that we can count or tokenise
# from sklearn.naive_bayes import MultinomialNB #helps in classifying the data distributed in different levels

# r1=["didn't meet the expectation", "waste of money", "loved the product", "poor quality don't buy it","product was good and amazing",'product is not good and broken', "excellent product", "recommended", "great product", "extremly dissatisfied", "loved the way you fool us", "loved the way you cheat", "delivered in perfect way" ]

# sentiments=np.array([0,0,1,0,1,0,1,1,1,0,0,0,1])
# vectr=CountVectorizer()
# matrix=vectr.fit_transform(r1)
# model=MultinomialNB()
# "applying the testing"
# model.fit(matrix,sentiments)

# def classifyNewReview(r2):
#   r2_vector=vectr.transform([r2])
#   predict=model.predict(r2_vector)
#   if predict[0] == 1:
#     print("+ve"),
#     return "Postive"
#   else:
#     print("-ive")
#     return "Negative"
    
# user_input=input("enter your review")
# result=classifyNewReview(user_input)
# print(f"this customer gave {result } feedback")