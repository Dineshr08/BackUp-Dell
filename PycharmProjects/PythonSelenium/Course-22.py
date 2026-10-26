# inheritance - invoking parent class variable and method to child class
# need to use import function in child class
# if parent class have parametrised constructor, then in child class under default constructor, need to define parent constructor


from ParentClass import Calculator1 # qaccessing parentclass data to here


class Child(Calculator1):  # inherited parent class
    num2 = 10

    def __int__(self):
        Calculator1.__init__(self, 10, 20) # parent constructor calling

    def add2(self):
        return self.num2 + self.add1() # accessing parent class variable and methods


objChild = Child()
print(objChild.add2())
