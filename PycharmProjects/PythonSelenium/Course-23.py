#String

Str = "Hi this is tamil"
Str1 = "tamil"
#get the first letter of str
print(Str[0])
#get the sub string  of str
print(Str[0:4])
#concatinate 2 string
print(Str1+Str)
#to check if string is present in another string
print(Str1 in Str)
# split the string using special character
Str2=Str.split(" ")
print(Str2)
#remove the white space in begenning and end of the string
Str3 = " Tamil"
print(Str3.strip())
#remove the white space in begenning  of the string
Str3 = " Tamil"
print(Str3.lstrip())
#remove the white space in end  of the string
Str3 = "Tamil "
print(Str3.rstrip())