#Fixtures - Which is same as setup and tear down in jmeter
#if we have 5 test cases here after 3rd test case we have fixture called , then first 3 test case will run , then fixture based on setup will run
import pytest


def test_case1():
    print("case1")


def test_case2():
    print("case2")


@pytest.fixture() # declaring fixture method
def case3(): #for fixture method , no need to give test before in method name
    print("setup case3")
    yield
    print("tear down") #declaring teardown, no need to call any where automatically run , once case4 test case finished

def test_case4(case3): #calling setup, when this file run, after case 3 only case4 will run
    print("case4")

def test_case5():
    print("case5")

