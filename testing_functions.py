# bring in pytest into virtual env using pip
# define tests with "test_<testname>()"  - see below

def find_largest(x, y):
    if x > y:
        return x
    else:
        return y

def test_find_largest():
    assert find_largest(1, 2) == 2       

def test_something():
    assert "test" == "test"