import matplotlib.pyplot as plt
import numpy as np

x=["JS", "Java", "Python", "Kotlin", "c#"]
y=[95,80,92,90]
z=[80,55,30,60]
# plt.plot(x,y)
"to add colors use"
colr=["red", "yellow","orange", "green", "blue", "pink"]
width=0.1
p=np.arange(len(x))
pi=[j+width for j in p]
plt.xlabel("languages")
plt.ylabel("polpularity")
plt.title("2024 survey on languages", fontsize=10)

'alpa for opacity 0-1'
# plt.bar(x,y,color=colr, width=.54, align="edge", edgecolor="r", linewidth=1, linestyle=":", alpha=.5)
"we can use label in two ways"
# plt.bar(x,y,color=colr, width=.54, align="edge", edgecolor="r",label="Test")
# plt.legend()
# plt.bar(x,y,color='green', width=.54, align="edge", edgecolor="r")
# plt.legend("y")

# plt.bar(x,y,color='green', width=width, align="edge" , label="Test")
# plt.bar(pi,z,color='red', width=width, align="edge", label="Test1")
# plt.xticks(p+width,x, rotation=40)
'horizontal bar graph'

# plt.barh(x,y, label="Test")
# plt.barh(pi,z,  label="Test1")
# plt.legend()
# plt.show()

"""
scatter plot 
"""
a=[11,22,33,14,25,26,17,18,29,10]
b=[9,8,7,6,5,4,3,2,1,0]
c=[8,7,5,4,5,8,7,9,6,3]
e=[11,12,15,11,4,2,3,6,5,10]
colss=[10,52,22,33,66,55,44,88,99,77]
# plt.title("scatter Plot", fontsize=10)
# plt.xlabel("days")
# plt.ylabel("frequency")

# plt.xticks(rotation=25)
# # plt.scatter(a,b ,c="orange", alpha=.7, marker="*", edgecolors="green", linewidths=1)
# plt.scatter(a,b ,c=colss, cmap='seismic')
# plt.scatter(a,c ,c="red")
# plt.scatter(a,e ,c="blue")
# plt.colorbar()
# plt.show()

"""
HISTOGRAM CHART IN MATPLOTLIB
"""
l=[5,10,15,20,25,30,35,40,45,50,55,60,65]
# x=np.random.randint(10,60,(50))
# plt.hist(x, bins=l, edgecolor="red")
# plt.hist(x, "auto",(0,50), edgecolor="red", cumulative="-1")
# plt.hist(x, edgecolor="red", histtype="step", orientation="horizontal", rwidth=0.4)
# plt.hist(x, edgecolor="red", orientation="horizontal", rwidth=0.4)
# plt.show()

"Matplotlib Pie Chart / Plot"
ex=[0.09,0.0,0.0,0.0,0.0]
x1=np.random.randint(10,60,(5))
'explode will pop out the sector from the circle'
plt.pie(x1,labels=x, explode=ex, autopct="%0.1f%%", radius=1, labeldistance=1.2)
plt.show()