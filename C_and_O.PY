#Creating the class
class Student:
    name= "Rachit Poudel","Sparsha","Rabin"
    RollNumber = 12,13,14,
    Address = "Kathmandu",

#Creatimg the Objects
s1 = Student()
print(s1.name)
print(s1.RollNumber)
print(s1.Address)

#creating the class
class student:
    def __init__(self,name): # this function is called when an object of a class is created
        self.name = name

#Creating the Objects
s1 = student("John Doe")
print(s1.name)