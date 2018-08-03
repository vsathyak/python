def greet(name, msg = "Good morning!"):
   """
   This function greets to
   the person with the
   provided message.

   If message is not provided,
   it defaults to "Good
   morning!"
   once we have a default argument, all the arguments to its right must also have default values.
   """

   print("Hello",name + ', ' + msg)

greet("Kate")
greet("Bruce","How do you do?")

#How to define function when we dont know how many arguments that will be passed
def greet(*names):
   """This function greets all
   the person in the names tuple."""

   # names is a tuple with arguments
   for name in names:
       print("Hello",name)

greet("savio","Alex","Dinkle","Baby")

# An example of a recursive function to
# find the factorial of a number
def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))
num = 4
print("The factorial of", num, "is", calc_factorial(num))

#normal functions are defined using the def keyword, in Python anonymous functions are defined using the lambda keyword.
#Syntax of Lambda Function in python --> lambda arguments: expression

double = lambda x: x * 2
print("Lambda Function", double(5))