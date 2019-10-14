name = 'Rich'
age = 55
print(f"Hello my name is {name}, I am {age} ")

print(f"{2 * 37}")

def to_lowercase(input):
    return input.lower()

print(f"{to_lowercase(name)} is my name spelled in lowercase")    # can call a defined function inside the {} braces

print(f"{name.lower()}")   # can call a built-in function inside the {} braces

class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        print("Comedian: __str__(self)")
        return(f"{self.first_name} {self.last_name} is {self.age}")

    def __repr__(self):                      # the “official” string representation of an object.
        print("Comedian: __repr__(self)")
        return(f"{self.first_name} {self.last_name} is {self.age}")

new_comedian = Comedian("Monty", "Python", 532)
print(f"{new_comedian}")
print(f"{new_comedian!r}")

# name = "Eric"
# profession = "comedian"
# affiliation = "Monty Python"
# message = (
#     f"Hi my name is {name}. \n"
#     f"I am a {profession}. \n"
#     f"I star on the {affiliation} show."
# )
# print(message)

# message = f"""
#     Hi my name is {name}.
#     I am a {profession}.
#     I star on the {affiliation} show.
# """
# print(message)

print(f'{"Eric Idle"}')