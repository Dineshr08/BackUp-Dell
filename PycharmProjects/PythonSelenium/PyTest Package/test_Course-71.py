# how to run particular file alone in path
# py.test filename.py -v- s ie in path only give file only run
# out of path, we will have multiple file, in each file multiple test cases will be there(method), out of multiple test case only need to run few test case, we can right regular expression and run
# py.test -k regname to filter -v -s eg py.test -k card -v -s


def test_hellocard():
    print("hello")

def test_haicard():
    print("hai")


def test_greet1():
    print("greet1")