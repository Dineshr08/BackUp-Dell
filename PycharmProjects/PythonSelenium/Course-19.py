# Functions,Function should be declared using def keyword

def welcome():
    print("Hello")
# Calling the function
welcome()

#Passing parameter to function
def welcome(name):
    print("Hello", name)
# Calling the function
welcome("Tamil")

def add(a, b):
    print(a+b)

add(2,3)

#Using return statement

def add(a, b):
    return a+b # if we give return here this output will get stored in function calling place

print(add(2,3))
# Or do like below, both are same
x = add(2,3)
print(x)


