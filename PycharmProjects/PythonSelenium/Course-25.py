#Open file and read or write data
file = open('test.txt') # open is to open file and store info in file object
#read all the data stored in file
print(file.read())
#read only few characters of file
print(file.read(5))
#Read only first line of file
print(file.readline())
#read all line in file

line = file.readline() # have first line value

while line!= "":
    print(line)
    line = file.readline()

#read all line in file using filelines method.it will store all the data in a file in list

line1 = file.readlines()
print(line1)

for i in file.readlines():
    print(i)

file.close() # always close the file post use