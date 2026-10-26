#conftest - if we have fixture and we need to pass that fixture to many files, so what we can do is we can create one conftest file and keep our fixture code there. so when u run the test case, it will automatically take from that place
# no need to create some common fixture for each test case

#imp note : Start with Test while writing class name too like TestExample1
import pytest

# if we have multiple test case like 100, so in that case no need to pass fixture name in all test case, for that we can create a class and class all method inside class and for that class, in general one fixture we can call like below
#imp note : Start with Test while writing class name too like TestExample1
#this fixture will applicable for all the method inside the clas


@pytest.mark.usefixtures("case3")
class TestCourse:

    def test_greetings(self):
        print("testing1")
    def test_welocme(self):
        print("testing2")

#if we want to apply fixture only for the once for class, but not for all method
#need to define scope="class" in conftest file

@pytest.mark.usefixtures("setup")
class TestCourse1:

    def test_greetings1(self):
        print("testing1")
    def test_welocme1(self):
        print("testing2")