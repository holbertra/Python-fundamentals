# Try Except

# def proclaim_user_birthday(name, age):
#     try:
#         new_age = age + 1
#         message = f'{name} is now {new_age} years old!'
#         print(message)
#     except Exception as e:    # Exception Type
#         print(e)
#     print("ONLY WHEN MY PROG CONTINUES")   

# proclaim_user_birthday("Rich", 55)
import pytest

def find_user(user_id):
    if not isinstance(user_id, int):
        try:
            user_id = int(user_id)
            print(user_id, "good cast")
        except Exception as e:
            raise TypeError("user_id must be a number")  # - Exits here
    return "A user" 
    #handle looking up the user here  

def test_find_user_returns_string():
    assert find_user(2) == "A user"

def test_find_user_takes_string_returns_string():
    assert find_user("2") == "A user"

def test_find_user_exception():
    with pytest.raises(TypeError):
        find_user("string")

# find_user(12) 
# find_user("adshjasdf") 
# find_user([])        
