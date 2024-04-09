import pandas as pd
"series in pandas"
x=[1,2,3,4,5,6,7,8]
# a=pd.Series(x)
# a=pd.Series(x, index=['a','b','c','d','e','f','g','h'], name="test data")
# print(a)

dic ={"name":["python",'cplus',"js"], "rating":[4,3,5]}
# print(pd.Series(dic)) 

# print(pd.Series([0,25,65,98,55]))
# print(pd.Series([0,25,65,98,55],index=[1,2,3,4,5]))
"""
why we use series instead of numpy array"""
x=(pd.Series(9,index=[1,2,3,4,5]))
y=(pd.Series(9,index=[1,2,3,4,5,6,7,8,9]))
# print(x+y)


"""
dataframes in pandas and airthmatic operation
"""

l=[1,2,3,4]
d={"name":["su","bis", "kes","dim"], "rating":[5,5,5,5]}
# print(pd.DataFrame(l))
# print(pd.DataFrame(d))
# print(pd.DataFrame(d, columns=["name"]))

d1={"a":[1,2,3,4], "b":[5,5,5,5]}
x=(pd.DataFrame(d1))
x["c"]=x["a"]+(x["b"])
# print(x)
"logical data handle checking which data is less than 20"

d1={"a":[11,22,33,44], "b":[50,15,25,35]}
x=(pd.DataFrame(d1))
x['checking']=x['b']>=20
# print(x)


"""
del and insert in pd
"""
'inserting 50 in new column'
# x.insert(1,"phtyon", 50)
'using list but size must be equal'
# x.insert(1,"phtyon", [11,22,33,65])
'copying and showing limited data using slicing // here only upto two index'
x['new']=x['a'][:2]

'deleting the data of b, will show the data deleted'
x1=x.pop('b')
# print(x1, x)


"""
writing the csv file 

"""

dis={1:[1,5,3,6,9,], 2:[4,5,6,9,5], "d":[4,5,69,8,5]}

x= pd.DataFrame(dis)
print(x)