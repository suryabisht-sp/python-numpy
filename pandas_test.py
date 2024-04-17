# import pandas as pd
# "series in pandas"
# x=[1,2,3,4,5,6,7,8]
# # a=pd.Series(x)
# # a=pd.Series(x, index=['a','b','c','d','e','f','g','h'], name="test data")
# # print(a)

# dic ={"name":["python",'cplus',"js"], "rating":[4,3,5]}
# # print(pd.Series(dic)) 

# # print(pd.Series([0,25,65,98,55]))
# # print(pd.Series([0,25,65,98,55],index=[1,2,3,4,5]))
# """
# why we use series instead of numpy array"""
# x=(pd.Series(9,index=[1,2,3,4,5]))
# y=(pd.Series(9,index=[1,2,3,4,5,6,7,8,9]))
# # print(x+y)


# """
# dataframes in pandas and airthmatic operation
# """

# l=[1,2,3,4]
# d={"name":["su","bis", "kes","dim"], "rating":[5,5,5,5]}
# # print(pd.DataFrame(l))
# # print(pd.DataFrame(d))
# # print(pd.DataFrame(d, columns=["name"]))

# d1={"a":[1,2,3,4], "b":[5,5,5,5]}
# x=(pd.DataFrame(d1))
# x["c"]=x["a"]+(x["b"])
# # print(x)
# "logical data handle checking which data is less than 20"

# d1={"a":[11,22,33,44], "b":[50,15,25,35]}
# x=(pd.DataFrame(d1))
# x['checking']=x['b']>=20
# # print(x)


# """
# del and insert in pd
# """
# 'inserting 50 in new column'
# # x.insert(1,"phtyon", 50)
# 'using list but size must be equal'
# # x.insert(1,"phtyon", [11,22,33,65])
# 'copying and showing limited data using slicing // here only upto two index'
# x['new']=x['a'][:2]

# 'deleting the data of b, will show the data deleted'
# x1=x.pop('b')
# # print(x1, x)


# """
# writing the csv file 
# will produce the csv file in the current folder, index=false will remove the index from the file
# """

# dis={"a":[1,5,3,6,9,], "b":[4,5,6,9,5], "d":[4,5,69,8,5]}

# x= pd.DataFrame(dis)
# # x.to_csv("csv1.csv",index=False)
# 'it will produce the header with given new name in the file'
# # x.to_csv("csv1.csv",index=False, header=["a","b","c"])  

# # print(x)


# """
# reading the csv file using pandas
# """

# # csv_file=pd.read_csv('//home//user//Documents//python//first//csv1.csv', usecols=['Name'])
# # csv_file=pd.read_csv('//home//user//Documents//python//first//csv1.csv', nrows=1)
# # csv_file=pd.read_csv('//home//user//Documents//python//first//csv1.csv', skiprows=[0,1,4])
# # csv_file=pd.read_csv('//home//user//Documents//python//first//csv1.csv', index_col='Name')
# 'will make particular row as header'
# # csv_file=pd.read_csv('//home//user//Documents//python//first//csv1.csv', header=2)
# 'make particular heading'
# # csv_file=pd.read_csv('//home//user//Documents//python//first//csv1.csv', names=["Surya's Data","Kesh","har"])
# # csv_file=pd.read_csv('//home//user//Documents//python//first//csv1.csv', header=None)
# # csv_file=pd.read_csv('//home//user//Documents//python//first//csv1.csv', dtype={'class':"float"})
# "will show the range of index"
# csv_file=pd.read_csv('//home//user//Documents//python//first//csv1.csv')
# # print(csv_file.index)
# 'will show the names of all the columns'
# # ""print(csv_file.columns)
# "to find min, max 50% 70%"
# # print(csv_file.describe())
# "starting 5 dataa"
# # print(csv_file.head())
# "last five"
# # print(csv_file.tail(2))
# "want to see particular range data"
# # print(csv_file[2:4])
# "show index in an array"
# # print(csv_file.index.array)
# "convert the data in numpy array"
# # print(csv_file.to_numpy())
# "sorting the data"
# # print(csv_file.sort_index(axis=0, ascending=False))
# "changing the in the column"
# # x=csv_file["Name"][0]="Surya"
# # print(x)
# # print(csv_file)
# # y=csv_file.loc[0,"Name"]="Kesh"
# # y=csv_file.loc[[1,2],["Name", "class"]]
# # print(y)
# # print(csv_file)
# "locating and priting particular data and then whole column"
# # y=csv_file.iloc[0,0]
# y=csv_file.drop("class", axis=1)
# # print(y)

# """
# handling the missing data using dropna and fillna
# """
# 'will drop the blank values or row'
# # print(csv_file.dropna())
# # print(csv_file.dropna(axis=1))
# # print(csv_file.dropna(axis=0))
# "if any row blank or blank data it will remove the row with how='any'"
# # print(csv_file.dropna(how="any"))
# "if use all it will remove the blank row only"
# # print(csv_file.dropna(how="all"))
# "will remove single null value or acc to given value"
# # print(csv_file.dropna(thresh=1))
# "fill na value with data"
# # print(csv_file.fillna("all"))
# "making condition to fill data in columns"
# # print(csv_file.fillna({"Name":"all", "class":"first", "status":"suspended"}))
# "filling the empty with the previous data of row"
# # print(csv_file.fillna(method="ffill", axis=1))
# # print(csv_file.fillna({"Name":"all", "class":"first", "status":"suspended"}))



# """
#   handling the missing data replace and interpolate
# """

# # print(csv_file.replace(to_replace=3, value=8))
# # print(csv_file.replace(to_replace="ssss", value="kesh"))
# # print(csv_file.replace("[A-Za-z]", "Saurya", regex=True))
# # x=csv_file.replace({"Name":'[A-Za-z]'},22, regex=True)
# 'replacing 2 with backward filling'
# # x=csv_file.replace(3, method="bfill")
# # x=csv_file.replace(1, method="bfill", limit=1)
# "inplace it will not create a copy of the data instead make the modification in the data itself"
# # x=csv_file.replace(1, method="bfill", limit=1, inplace=True)
# "interpolate work with only numeric value"
# # x=csv_file.interpolate()
# "must have same data type in col for axis 1"
# # x=csv_file.interpolate(method="linear", axis=0)
# # x=csv_file.interpolate(limit_direction="backward", limit=2)
# "outside will fil all na numeic value while inside will keep the na data"
# # x=csv_file.interpolate(limit_area="outside")
# "replacing the data in orignal"
# # x=csv_file.interpolate(limit_direction="forward", limit=3, inplace=True)
# # print(csv_file)

# """
# Merge and Concat DataFrames using pandas, but must have one column common its because it will merge all data else it will merge that data which is common
# """
# dis1=pd.DataFrame({"a":[11,51,31,6,9,], "b":[41,51,61,19,5], "d":[4,5,69,8,5]})
# dis2=pd.DataFrame(dis)
# # car=pd.merge(dis1,dis2,on="d" )
# # print(car)
# 'print the missing values'
# dis1=pd.DataFrame({"a":[11,51,31,6,9,], "b":[41,51,61,19,5], "d":[4,5,69,8,5]})
# dis2=pd.DataFrame({"a":[11,51,3,6,9,], "b":[4,5,6,9,5], "d":[4,5,69,8,5]})
# 'will show only those which are common on all'
# # car=pd.merge(dis1,dis2, how="inner" )
# 'will show all data'
# # car=pd.merge(dis1,dis2, how="outer", indicator=True )
# 'you can change the heading name '
# # car=pd.merge(dis1,dis2, left_index=True, right_index=True, suffixes=['name','id'] )
# # print(car)


# "concatination of dataframes"
# a=pd.Series({"a":[1,2,3,4],"b":[4,8,5,6]})
# b=pd.Series({"a":[1,5,4,6],"b":[9,8,7,6]})
# # print(pd.concat([a,b],axis=1))
# # print(pd.concat([a,b],axis=0  ))

# """
# Pandas GroupBy - Guide to Grouping Data
# """

# d=pd.DataFrame({"Name":["a","b","c","e", "a","b","e"], "Hindi":[50,50,52,60,50,50,90], "English":[70,80,90,55,70,80,90]}) 
# a=d.groupby("Name")
# # for x,y in a:
# #   print(x)
# #   print(y)
# 'get the data of particular group'
# # print(a.get_group("a"))
# # print(a.max())
# # print(a.mean())
# "convert the data into list"
# # print(list(a))

# """
# Join and Append DataFrames
# """
# s=pd.DataFrame({"a":[1,2,3,4],"b":[4,8,5,6]})
# d=pd.DataFrame({"c":[1,5,4,6],"e":[9,8,6,5]})
# # print(s.join(d, how="left"))


# "Pivot Table and Melt Function-------------------"
# d=pd.DataFrame({"days":[1,1,2,2,1,1,2],
#                 "Name":["a","b","b","a", "a","b","b"], 
#                 "Hindi":[50,50,52,60,50,50,90], 
#                 "English":[70,80,90,55,70,80,90]}) 
# "providing id, it will treat that particular column as id and show its data"
# # print(pd.melt(d, id_vars=["Name"], var_name="Surya", value_name="sp"))

# "Pivot"
# # print(d.pivot(index="days", columns="Name"))
# # print(d.pivot_table(index="days", columns="Name", aggfunc="mean"))
# # print(d.pivot_table(index="days", columns="Name", aggfunc="mean" , margins=True))
# print(d.pivot_table(index="days", columns="Name", aggfunc="median" , margins=True))
