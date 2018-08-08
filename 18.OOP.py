#Person -->class
# name -->property
#self represents the instance of the class. By using the "self" keyword we can access the attributes and methods of the class
#It binds the attributes with the given arguments.
class Person:
    def __init__(self, name, age): #__init__() is used to initialize a newly created object to the class
        self.name= name
        self.age= age
    def getName(self):
        print("Your name is:" +self.name)
    def getAge(self):
        print("Your age is:" +self.age)

p1=Person("savio","30")
p1.getName()
p1.getAge()