#Validate the test case.if test case did not get expected result how to fail the test case.2 methods are there one is assert and raise Exception

#Rasie Exception

Item = 0

#we are failing test case if item is not equal to 2

if Item!= 2:
    raise Exception("Do not have enough Items")

# Assert - Same we are failing test case using assert

assert (Item == 2)