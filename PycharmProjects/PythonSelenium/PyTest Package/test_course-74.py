#conftest - if we have fixture and we need to pass that fixture to many files, so what we can do is we can create one conftest file and keep our fixture code there. so when u run the test case, it will automatically take from that place
# no need to create some common fixture for each test case

def test_course74_case1(case3): #here it aytonatically look fixture from conftest file
    print("test_course74_case1")


def test_course74_case2(case3):  # here it aytonatically look fixture from conftest file
    print("test_course74_case2")