class Calculator1:
    num1 =10  # class variable

    def __init__(self, a, b): # default constructor
        self.a = a
        self.b = b
        print("This is default constructor, it will execute first")
    def add1(self):
        print("adding two values")
        return self.a + self.b + self.num1

