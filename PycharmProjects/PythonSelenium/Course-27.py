#read the data from file then reversed then write back to file

with open('test.txt', 'r') as file:  # same as file open and close #reading file
    line = file.readlines()
    line1 = reversed(line) # data stored in line will be in list which will be revered
    with open('test.txt','w') as file1: # writing to file
        for i in line1:
            file1.write(i)
