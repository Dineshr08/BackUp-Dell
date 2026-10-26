#if loops

a = 5

if a < 2:
    print("a is less than 2")
else:
    print("a is greater than 2")
print("if condition completed")

#For loop , its used to iterate all element in list and iterate till the range which we defined

obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i)
print("for loop completed")

#for loop using range

for j in range(1, 5): # here 5 means it will iterate till 4
    print(j)
print("for loop with range completed")

#for loop using range with for(i=0;i=i+2;i++)

for k in range(1, 5, 2): # here 5 means it will iterate till 4
    print(k)
print("for loop with range with increment completed")

#for loop using range without initial number

for l in range(5): # here 5 means it will iterate till 4
    print(l)
print("for loop with range1 completed")

#While loop

m = 10

while m >= 1:
    if m == 9:
        m = m-1
        continue # skips that current iteration, it wont go down and starts from top
    if m == 3:
        break # break that complete loop, after this no further iteration will run
    print(m)
    m = m-1
print("while loop completed")

