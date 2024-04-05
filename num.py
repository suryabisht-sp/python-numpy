import numpy as np

# """
# array
# """

# x= np.array([1,2,3,4,8])
# print(x)
# print(type(x))



# """
# python list
# """
# # %timeit[j**4 for j in range(1,9)]
# x= [1,2,3,4,8]
# print(x)
# print(type(x))





"""
append array
"""

# x= [] 

# for i in range (1,6):
#   y = input("enter the num :")
#   x.append(int(y))
# print((np.array(x)))


"""
creating a zero matrix with np and 5*5
# """

# x= np.zeros((5,5))

# x= np.zeros(4)

# print(x)


"""
for singular matrix with np
"""

# x = np.ones(4)
# print(x)

# x=np.ones((4,5))
# print(x)




"""
for empty matrix with np, you will see your previous data will show in the print
"""

# x = np.ones(4)
# print(x)

# x=np.ones((4,5))
# print(x)




"""
for matrix with range np, it will create array in continous order
"""

# x = np.arange(4)
# print(x)




"""
for identity matrix with np, means diagonal elements will be 1
"""

# x = np.eye(2)
# x = np.eye(2,4)
# print(x)




"""
for linspace random numbers with equal steps
here 0,20 means range and num 5 is the steps or equal parts
"""

# x = np.linspace(0,20, num=5)
# print(x)


"""
for numpy arrray with random numbers 
rand generate between 0 to 1
randn generate close to zero (+ve and -ve both numbers)
ranf between 0.0 to 1.0 where 1 is not inculded
randint random number between given range
"""

# x = np.random.rand(1)
# print(x)

# x = np.random.rand(2,5)
# print(x)


# x = np.random.randn(1)
# print(x)


# x = np.random.ranf((2,4))
# print(x)


x = np.random.randint(20,100,100)
print(x)