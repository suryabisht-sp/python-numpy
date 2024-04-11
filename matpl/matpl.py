import matplotlib.pyplot as plt
import numpy as np

x=["JS", "Java", "Python", "Kotlin"]
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

plt.barh(x,y, label="Test")
plt.barh(pi,z,  label="Test1")
plt.legend()
plt.show()