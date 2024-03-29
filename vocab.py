# Vocabulary

"""
f strings https://cito.github.io/blog/f-strings/
interpreter
variable
number - 3 types:  int, float, complex
string - immutable (a type of class behind scenes in python )
integer
float - rational
boolean - true/false
modulus - % keep the remainder
arithmetic operator -  +, /, *, -, %, **
floor division - x // y
assignment operators - 
concatenation - 
string templating - plugging valid python code directly into f-strings
conditional - statement that resolves to true or false
immutable - cannot be changed
mutable - can be changed
if - When a condition is met, execute following code
elif - If preceding if and elif statements do not execute & this condition is met
else - Default conditions, execute following code
Three number data types: int, float, complex

Collections: 4 types: list, tuple, set, dict
lists -      mutable,   ordered, collection of data, use square brackets [ ]
    operations:
    concatenation: [1, 2, 3, 4] + ['apples', 'oranges'] + ['Alice', 'Bob']
    reverse:   List_name.reverse()
    append:    List_name.append()
    split:     List_name = List_name.split()  !!!Note, has to be re-assigned!
               You cannot do this: 
                    List_name.append()
                    print(List_name[0])  !! This will only print first letter of the string
                                            NOT the first word of the string which is what you want.
    sorting:   List_name.sort()
    joining:   
    create a list of numbers:  numbers = list(range(10))
    
               

tuple -      immutable, ordered, type of list, use ( a, b, c )
set -        mutable,   unordered, use curly braces {, , } ex. dictionary , multiple data types
dictionary - mutable,   unordered, set of key-value pairs denoted by { } braces
    operations:
    unpacking: 
    favorites = {'fruit':'apples', 'animal':'cats', 'number':42}
    for k,v in favorites.items():
        print(k, v)

    multiple assignments: str1, str2, str3 = ['apples', 'cats', 42]
    
    listing contents:
    print(list(favorites.keys()))    # using list statement gets rid of the dict_items(. . .) print out
    print(list(favorites.values()))
    print(list(favorites.items()))

    

for loop - block code executed over the number of items specified in a sequence

/* FUNCTIONS */
functions - A named reusable block of code that can take in and return information
scope - A bounded region that contains local information but can access information
        from it's parent scope ( bad practice)
parameters - What a function asks for in the definition - (what is received)
argument - What you pass into the function -              (what is passed)
    def func(parameters):  - receiving side
    func(arguments)        - calling side
return - Data that is passed back from a function, 
         it not stated explicitly there is always a default (None)
code block - Region that is indented - indentation is the signal to end
procedure - Sequential steps for performing actions - its reusable

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

# Virtual environment
# isolated environ in python used to test and share projects in to order
# keep dependencied local

String interpolation - a process substituting values of variables 
into placeholders in a string. For instance, if you have a template 
for saying hello to a person like "Hello {Name of person}, nice to meet you!", 
you would like to replace the placeholder for name of person with an actual name. 
This process is called string interpolation.

#### YES/NO QUESTION: A way of asking a y/n question ####
print('Do you want to play again? (yes or no)')
return input().lower().startswith('y')

STRING OPERATIONS:
Writing to an Empty string:
    my_string = ""
    my_string += "Hello World"


Printing: One string on top of the other; use carriage return \r, suppress the \n
print('Print this sentence. . .\r', end="" )
print('Now print this over top. . .')
-- OR --
os.system('cls' if os.name == "nt" else "clear")  # clear screen before each new print

"""