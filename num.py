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


# x = np.random.randint(20,100,100)
# print(x)




"""
Arithmetic operation 
"""

# var = np.array([1,2,3,4])
# varb= np.array([1,2,3,4])
# result = var+ varb
# print(result)

# result = var  % 2
# print(result)

# result = var **3
# print(np.add(var,varb))
# print(result)



"""
Arithmetic operation  in 2d array
"""
# var = np.array([[1,2,3,4],[1,7,3,4]])
# varb= np.array([[1,2,3,4],[1,29,3,4]])
# result = var+ varb
# print(np.reciprocal(var))
# # print(result)



"""
Arithmetic operation 
"""
# var = np.array([1,2,3,4,5,6,7,8,9,6,5,6,91])
# var = np.array([[1,2,3,4],[1,7,3,4]])
# print(np.min(var))
var = np.array([1,7,3,4])
"axis 0 means column and 1 means rows"
# print(np.min(var, axis=0))
# print(np.max(var, axis=0))
# print(np.max(var))
# print(np.argmin(var))
# print(np.argmax(var))
# print(np.sqrt(var))
# print(np.sin(var))
# print(np.cos(var))
"here its provide commulative addition of each element of row "
# print(np.cumsum(var))


"""
shape and reshaping in numpy
"""
# var = np.array([[1,2,3,4],[1,7,3,4]])
# print(var.shape)

"for creating multi dimension us ndmin below we provided 8 means 8,8 or 8*8"
var = np.array([1,7,3,4], ndmin=8)
# print(var.ndim)
# print(var.shape)
"here output will be (1,1,1,1,1,1,1,1,1,1,4) which means we have only one row in and 4 column only"

"Reshaping the array"

# var = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
# var = np.arange(16)
var = np.arange(64)
# print(var.ndim)
"here 2,2 means matrix for array"
# x = var.reshape(4,2,2)
x = var.reshape(2,2,4,4)
"""make sure element must meet the criteria for making matrix iee if 1d have 4 
element then we can make it 2*2 if we want 3*3 the be must have 9 elements in array for that.
"""
# print(x)
# print(x.ndim)
# one= x.reshape(-1)
# print(one)


"""
broadcasting 
"""

x= np.array([1,2,3])
y=np.array([[1],[2],[2]])

# print(x,"\n",y)
# print(x.shape,"\n",y.shape)
# print(x+y)


"""indexing and slicing the array"""

var = np.array([[1,7,3,4],[1,2,3,4]])
# print(var)
# print(var[0,-1])


""""
iteration in array in numpy

"""

var = np.array([1,2,3,4,5,6,7,8,9,6,5,6,91])
# for i in var:
#   print(i)

var1 = np.array([[1,7,3,4],[1,2,3,4]])
# for j in var1:
#     for k in j:
#       print(k)

"alternative"

# for i in np.nditer(var1):
#   print(i)
# for i in np.nditer(var1, flags=['buffered'], op_dtypes=["S"]):
#   print(i)

"data laong with index"
# for i,d in np.ndenumerate(var1):
#   print(i, d)



"""
copy funtion in np
"""



var = np.array([1,2,3,4,5,6,7,8,9,6,5,6,91])
car1= var.copy()
car2= var.view()
var[1]=69
# print(car1, "\n", car2)

"""
concatination of data
"""



var = np.array([6,5,6,91])

var1 = np.array([1,2,3,4])

# print(np.concatenate((var,var1)))
# print(np.hstack((var,var1)))
# print(np.vstack((var,var1)))
# print(np.dstack((var,var1)))

# print(np.array_split(var1,4))

var = np.array([1,2,3,5,6,7,8,9])
# print(np.where(var==5))
# print(np.where(var%2==0))

"search and sort"

# print(np.searchsorted(var1,4))
# print(np.searchsorted(var1,4, side="left"))

var = np.array([2,1,3,4,6,5,8,7,7])

# print(np.sort(var))

# np.random.shuffle(var)
# x=np.unique(var)
# x=np.unique(var,return_index=True, return_counts=True)
"""
flatten and ravel
"""
# print(x)



"""
insert and delete array
"""

var = np.array([[2,1,7],[5,6,9]])

# x =np.insert(var, 0, 40)

# print(x)

# x =np.insert(var, (1,2), 40)

# print(x)

# x =np.insert(var, 1, 40, axis=1)

# print(x)


# x =np.insert(var, 1, [40,10], axis=1)

# print(x)

# x =np.delete(var,1)

# print(x)


"""
matrix in numphy
"""
var = np.matrix([[2,1,7],[5,6,9]])

# print(type(var))

var1 = np.matrix([[1,2],[3,4]])

var2 = np.matrix([[1,1,2],[3,4,4]])
var3 = np.matrix([[1,2],[3,4]])
# print(type(var1))
"normal multiply of array/matrix"
print(var1*var2)
"dot mulitply of matrix" 
print(var1.dot(var2))
print()
print(np.transpose(var2))
print()
print(np.swapaxes(var2,0,1))
print()
"inverse of matrix"
print(np.linalg.inv(var3))
print()
"power of matrix"
print(np.linalg.matrix_power(var3,2))
print()
"indentity matrix"
print(np.linalg.matrix_power(var3,0 ))
print(np.linalg.matrix_power(var3,2))
"inverse of power"
print()
print(np.linalg.matrix_power(var3,-2 ))
"deteminate of matrix"
print()
print(np.linalg.det(var3))
