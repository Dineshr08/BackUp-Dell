#you have test case, that test case have to run for each set of data eg ur test case has to run on chrome, firefox and ie too . how to handle this using fixture conftest file


def test_parametrisation(runmultipletime):
    print(runmultipletime) # getting or passing all data , so this test case will run for 3 times, since we have 3 sets in fixture and print all data for each set run
    print(runmultipletime[1]) #print first index value for each set run