"# OOP-from-Python" \

## Class is the blue print for Creating Objects

## How the Class and Object are Created ?

Creating the class
    class student:
    name= "Rachit Poudel"

Creatimg the Objects
    s1 = student()
    print(s1.name)


__init__ Function 
Constructor: All classes have a function called __int__(),   which is always eecuted when the class is being initiated.

## creating the class
class student:
def __init__(self,name): # this function is called when an object of a class is created
self.name = name

## Creating the Objects
s1 = student("John Doe")
print(s1.name)

self parameter is a reference ro the current intance of the calss and is used to access variables the belongs to the class. 

## Del Keyword 
Used to delete the object properties or object itself.

## Class & Instance Attributes 

There is two type of attributes :
1. Class Attributes: The Attributes in class which  own and same to all objects.
2. Instance Attruibutes: The attributes which is different to the different object.

## Static Methods :

Methods that don't use the self parameter (Work at class level)
class method is called static method.
"Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function,without parmanetly modifying it.
**@staticmethod** is the decoder. it is the type of decoder that convert the normal function to static function/method.

## Private(Attributes and Methods)
Private attributes and methods are meant to be used only within the class and are not assiciable from outside of the class.

## Super Methods
super() method isused to access method of the parents class.

## Abstraction 
Hiding the implementaion details of a class and only showing the necessary features to the user.

# Inheritance
When the one class (child/derived) deives the properties and methods of the another class (parents/base).

**Types of inhetance**
1. Single Inheritance 
2. Multi-level Inheritance
3. Multiple Inheritance 


## Encapluation
Wrapping data and function into a single unit(Object)