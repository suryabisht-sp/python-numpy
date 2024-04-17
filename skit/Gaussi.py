# """
# Gaussian

# """
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.mixture import GaussianMixture
# from sklearn.preprocessing import StandardScaler

# np.random.seed(42)
# seg1 = np.random.normal(loc=30, scale=5, size=100)  
# seg2 = np.random.normal(loc=60, scale=10, size=150)  
# seg3 = np.random.normal(loc=90, scale=8, size=120)  
# data = np.concatenate([seg1, seg2, seg3]).reshape(-1, 1)

# # Fit and transform the scaler
# scaler = StandardScaler()
# data_scaled = scaler.fit_transform(data)
# n_component=3
# gmm=GaussianMixture(n_components=n_component,random_state=42)
# gmm.fit(data_scaled)
# resu=gmm.predict(data_scaled)
# plt.scatter(data, np.zeros_like(data), c=resu, cmap='viridis')
# plt.title("custer")
# plt.xlabel("purchase amt")
# # plt.show()
# user_iput=float(input("entert the data: "))
# user_input_sclr=scaler.transform(np.array([[user_iput]]))
# reso=gmm.predict(user_input_sclr.reshape(-1,1))[0]
# print("response is: ", reso)