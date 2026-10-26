# how to run using command line
# here in pytest all method will consider as individual test cases
# same method name should not be used
#command to run in command line py.test
#if we give py.test whatever pytest test case present in that path all will run together
#py.test only provide few data in output
#if you need more log then use py.test -v (v means verbose)
#if we want to see all the data like when u run in console like print statement etc need to use py.test -v -s

#this is one test case
def test_greet():
    print("good morning")

#this is second test case
def test_asser():
    msg = "hello"
    assert msg == "Hi", "Assertion falied, because it didnt matched"
    #"Assertion falied, because it didnt matched"  if assertion failed it will print.use , and we can give like this