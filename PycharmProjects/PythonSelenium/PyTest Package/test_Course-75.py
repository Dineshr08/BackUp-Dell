#getting the data from fixture conftest file and using in the method or test case
#earlier what we seen is , we no need to pass the fixture name in each method in class, if we declare on global, but when we retriving data from fixture conftest file from return statement, we need to pass the fixture name in method parametrized place

#imp note : Start with Test while writing class name too like TestExample1
import pytest


@pytest.mark.usefixtures("getdata")
class TestExample1:
    def test_edit(self, getdata):
        print(getdata)
        print(getdata[0])
        print(getdata[3])