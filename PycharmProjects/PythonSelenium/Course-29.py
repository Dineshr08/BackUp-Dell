#Try, Except and Finally
#this is mainly used if test case failed and still want our test case to continue
#Consider in our app, some time pop up will come and sometimes not, in that case keep pop up code in try and not pop up code in except.So in try if pop up comes try will run and skip except and continue to run and our test case wont fail.if no pop up comes , try block will fail but our test case wont fail and it go to except and run the test case.
#Finally: it will run irrespective of output of try and except

try:
    with open('test1.txt', 'r') as file:  # same as file open and close #reading file
        line = file.read()
except Exception as e:
    print(e)
    print("File not found")
finally:
    print("Its run always, irrespective of try or except")