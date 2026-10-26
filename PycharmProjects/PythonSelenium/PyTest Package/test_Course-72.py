# here we are going to see mark
#mark is like grouping, ie we can group the testcase like smoke test case, regression test case like that and uing that group name we can run that particular alone
# mark or grouping -@pytest.mark.smoke which is marking or group based on scenario, to run this py.test -m smoke -v -s
#if we want to skip one test cae ie we know that test case is failing and we want to ignore that test case during execution
# skip test case  - @pytest.mark.skip to run this py.test -v -s
#we know this test case failing but still we need that to run because its pre req for other test case, but it should not shown the result in report
#not to shown in report - @pytest.mark.xfail to run this py.test -v -s
import pytest


@pytest.mark.smoke
def test_hellocard1():
    print("hello")
@pytest.mark.skip
def test_haicard1():
    print("hai")

@pytest.mark.xfail
def test_greet2():
    print("greet1")