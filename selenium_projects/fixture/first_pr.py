from pytest import fixture

@fixture
def greet():
    print("hello world")


# passing fixture to test method
def test_greet(greet):     # passing fixture as an argument to test function
    return "hello world" == greet

