"# OOP-from-Python" \

Class is the blue print for Creating Objects

How the Class and Object are Created ?

Creating the class
    class student:
    name= "Rachit Poudel"

Creatimg the Objects
    s1 = student()
    print(s1.name)


__init__ Function 
Constructor: All classes have a function called __int__(),   which is always eecuted when the class is being initiated.

creating the class
class student:
def __init__(self,name): # this function is called when an object of a class is created
self.name = name

Creating the Objects
s1 = student("John Doe")
print(s1.name)

self parameter is a reference ro the current intance of the calss and is used to access variables the belongs to the class. 