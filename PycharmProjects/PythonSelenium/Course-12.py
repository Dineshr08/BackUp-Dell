#Data types
#there are numeric, string,list , tuple and dictionary data types we have
# in Numeric we have int, float and complex data type as sub type.Comples means a = 10+5j

#Concatinate two same data types we can use +

a = "Hello"
b = "world"
print(a+b)

#List data tpes
#List should be in Sq bracket
value = [5, 8, "Hello", 8.5, "Last"]
#Get first value of list
print(value[0])
#Get last value of list
print(value[-1])
#Get inbetween value  range of list
print(value[1:3])
#append - add the value to end of the list
value.append("Last1")
print(value)
#insert - insert the data to anywhere in list
value.insert(3,"Tamil")
print(value)
#update the existing index value
value[3] = "TAMIL" # updating to capital value
print(value)
#deleting the value in list
del value[3]
print(value)

#Tuple - is same as list but its immutable ie cant change the value in tuple like cant update,append. here we use () bracket to declare tuple
# values in tuple always fixed one
tup = (8,3,"Tamil",8.99,"Last")
print(tup[0]) # print value inside tuple

#Dictonary - Delcare dictonary in {}, it will be in key:value pair.if we define key or value as string it should be in " and while retrive also we should use "

dict = {"a": 5, 5: "test", "c": "Tamil"}
print(dict["a"])
print(dict[5])
#Adding the data to dictionary
dict["FName"] = "Dinesh"
dict["LName"] = "Rajendran"
print(dict)
#Create empty dictonary and add data to dictionary
dict1 = {}
dict1["FName"] = "Dinesh"
dict1["LName"] = "Rajendran"
print(dict1)