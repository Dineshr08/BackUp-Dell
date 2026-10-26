#Classes and object
#Class is the blue print of application, which has method(how it has to perform) and variable(what are the data it has to be to perform)
#Object is final out put of application when we run it
# Class will have method, variables(class variable and instance variable) and Constructor.
# variable inside class called class variable and variable inside method or constructor called instance variable
# variable passed to constructor called parametrised constructor
# constructor always defined as __init__
#When ever an object is created first a default constructor will run.if we didnt declare this too, it will run in backend during runtime'

class Calculator:
    num =10  # class variable

    def __init__(self): # default constructor
        print("This is default constructor, it will execute first")
    def add(self):
        print("adding two values")

obj = Calculator()  #obj is object of class Calculator
#calling class variable and method of class using object
obj.num
obj.add()


#Passing value
#data passed inside constructor called parametrised constructor
#We can create any number of objects and call to class
#whereever variable called inside method or constructor , it should be self.variable name, its for class variable too
#self is reffered as object, then that object variable, which is self.a
class Calculator1:
    num1 =10  # class variable

    def __init__(self, a, b): # default constructor
        self.a = a
        self.b = b
        print("This is default constructor, it will execute first")
    def add1(self):
        print("adding two values")
        return self.a + self.b + self.num1

obj1 = Calculator1(2,3)  #obj is object of class Calculator
#calling class variable and method of class using object
obj1.num1
print(obj1.add1())
obj2 = Calculator1(10,20)
print(obj2.add1())