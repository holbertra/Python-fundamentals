# Classes

# OOP - (Object Oriented Program)
# Four pillars of OOP  (APIE)
#   A(bstration) - Hiding lower level operations for user 
#                  Dealing with idea rather than Procedure
#   P(olymorphism) - Functions that operates differently depending on the data given
#   I(nheritance)  - Passing onto data & functionality in from parent class or object.
#                    Single Inheritance - from a single class/thing/parent
#                    Multi-level Inheritance - Chaining inheritance - ( layerd )
#                    Mulitple Inheritance - Class inherits several other classes ( 2 or more)  
#                    Heirachical Inheritance - When a class is inherited by multiple classes.
#   E(ncapsulation)- Data and functions that manipulate that data are bundled together.



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print("I sleep")

class Kid:
    def blah(self):
        print("I exist too") 

    def sleep(self):
        print("I sleep like a kid")


class Student(Person, Kid):     # Capitalized naming CAMEL

    counter = 0                # Class attribute
    school = "1150 Academy"    # Class attribute
    
    def __init__(self, name, grade, age):  # dunder only required method
        super().__init__(name, age)
#        self.name = name       # instance attribute - this is now defined in Person Class
        self.grade = grade      # instance attribute
#        self.age = age
        Student.counter += 1

    def have_birthday(self):
        self.age += 1

    def greeting(self):
        return f'Hello, my name is {self.name}. I am in grade {self.grade}. I am {self.age} yrs. old'

    def sleep(self):
        super().sleep()
        print("I sleep on books")

    def change_name(self, new_name):
        self.name = new_name


xzavier = Student("Justin", 8, 32) 
xzavier.name = "Xzavier"

print(xzavier.greeting())  

s1 = Student(0,1,3) 
s2 = Student(3,3,3) 
s3 = Student(9,0,9)

s3.sleep()

print(xzavier.counter)

name = "you"

def mod_name(to_change):
    to_change = "They"
    return to_change

name = mod_name(name)

# print(s1.counter)
# print(s2.counter)
# print(s3.counter)






