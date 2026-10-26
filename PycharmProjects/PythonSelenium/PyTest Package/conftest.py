import pytest


@pytest.fixture() # declaring fixture method
def case3(): #for fixture method , no need to give test before in method name
    print("setup case3")
    yield
    print("tear down") #declaring teardown, no need to call any where automatically run , once case4 test case finished


@pytest.fixture(scope="class") # declaring fixture method
def setup(): #for fixture method , no need to give test before in method name
    print("setup case3")
    yield
    print("tear down") #declaring teardown, no need to call any where automatically run , once case4 test case finished


@pytest.fixture()
def getdata():
    print("Getting data from fixture")
    return ["Dinesh","Tilaga","Amma","Appa","Abi","Tamil"]

#fixture  - passing parametrization
#you have test case, that test case have to run for each set of data eg ur test case has to run on chrome, firefox and ie too . how to handle this using fixture conftest file

@pytest.fixture(params=[("chrome","dinesh"),("firefox","tamil"),("edge","thilaga")]) #here () will consider one set, so we are running 3 sets , each set passing multipe data
def runmultipletime(request): #request the syntax
    return request.param #from this we are getting data from param
