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
    collage_name = "Herald Collage Kathmandu." #Class Attributes 
    def __init__(self,name,rollnumber): # this function is called when an object of a class is created
        self.name = name #Instance Attributes.
        self.rollnumber = rollnumber

# using @staticmethod to use the static method with out giveing the self parameter.
    @staticmethod
    def Hello ():
        print ("Hello Everyone.")
# Here self is a reference to the object

    def hello(self):
        print("Hello",self.name)

    def get_rollnumber (self):
        return self.rollnumber
#taking user input  to create the object 

name1 = input("enter the name of the student 1:")
rollnumber1 = input ("enter the RollNumebr of the Student 1:")
s1 = student(name1,rollnumber1)

name2 = input("enter the name of the student 2:")
rollnumber2 = input ("enter the RollNumebr of the Student 2:")
s2 = student(name2,rollnumber2)

#printing the details of the student 
print("The Details of ",s1.name,"are as follows : ")
print("Name : ",s1.name )
print("Roll Number : ",s1.rollnumber)
print(s1.collage_name)
print("\nThe Details of ",s2.name," are as follows : ")
print("Name : ",s2.name)
print("Roll Number : ",s2.rollnumber)
print(s1.collage_name)
s1.Hello() #Calling the static method to print in the console.
s2.hello()
s1.hello() # calling the method.
print(s1.get_rollnumber())
print(s2.get_rollnumber())



#Question for the methods :

class student:
    def __init__(self,name,marks):
        self.name =name
        self.marks =marks

    def get_average(self):
        sum = 0
        for val in self.marks:
            sum +=val
        print("HI",self.name,"Your avg score is",sum/3)

s1 = student("Sparsha",[60,55,60])
s1.get_average()

#Manupaliting  the attributes values.
s1.name = "Rachit"
s1.marks = [60,70,65]
s1.get_average()

# Abstration 

#Define a class named 'Car'
class Car:
    # Define the constructor method '__init__' which initializes the object's attributes
    def __init__(self):
        # Initialize attributes 'acc', 'brk', and 'clutch' to False
        self.acc = False  # Represents whether the accelerator is pressed
        self.brk = False  # Represents whether the brake is pressed
        self.clutch = False  # Represents whether the clutch is pressed

    # Define a method named 'start' to start the car
    def start(self):
        # Engage the clutch
        self.clutch = True
        # Turn on the ignition (start the engine)
        self.acc = True
        # Print a message indicating that the car has started
        print("Car Started....")

# Create an instance of the 'Car' class named 'car1'
car1 = Car()
# Call the 'start' method of the 'car1' object to start the car
car1.start()



class Student:
    def __init__(self,name):
        self.name
    
s1 = Student("rachit poudel")
del s1.name # it is used to delete the obbject attributes.



class person:
    __name = "Rachit" #Private Attributes

    def __hello(self):
        print("Hello",)

    def welcome(self):
        self.__hello()
    
p1 = person()
print(p1.welcome())


#Inheritance 


#Single Inheritance

class car:                     # parents class 
    color = "White"
    @staticmethod
    def start():
        print("CAr Started..")

    color2 = "black"
    @staticmethod
    def stop():
        print("CAr Stoped..")

class ToyotaCar(car):             #Child class 
    def __init__(self,name):
        self.name = name

car2 = ToyotaCar("Fortuner")
car3 = ToyotaCar("hilux")

#printing the values 
print(car2.color)
print(car2.start())
print(car2.color2)
print(car3.stop())

#Multi-Level Inheritance

class car:                     # parents class 
    @staticmethod
    def start():
        print("CAr Started..")

    @staticmethod
    def stop():
        print("CAr Stoped..")

class ToyotaCar(car):             #Child class 
    def __init__(self,brand):
        self.brand = brand

class fotuner(ToyotaCar):         # Child Class
    def __init__(self,type):
        self.type = type
        super().__init__(brand="Fortuner.") #  super calss to use the private parent class attributes.
        super().stop()
car4 = fotuner("Diesel")
print(car4.start())
print(car4.brand)



#Multiple Inheritance 

class A:
    varA = "Welcome to class A"
class B:
    varB = "Welcome to class B"
class C(A,B):
    varC = "Welcome to the class C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)



#Class Methods 

class Person:
    Name = "Rachit"

    @classmethod
    def changename(cls,name): # there cls is references to the classs Person.
        cls.Name = name
    
p1 = Person()
p1.changename("Sparsha")
print(p1.Name)

#property methods

class student:
    def __init__(self, compu, AI, collab):
        self.compu = compu
        self.AI = AI
        self.collab = collab


    @property
    def Percentage(self):
        return str((self.compu + self.AI +self.collab)/3) + "%"
    
st1 = student(65, 70, 75)
print(st1.Percentage)

st1.AI = 65
print(st1.Percentage)

# Polimorphism: (Operator overloading)

print(3+5) # answwer is 8 
print("Rachit" + "Poudel") # the Answer is Rachit Poudel concating the srtings.
print([1,2,3,4] + [6,7,8,9]) # the + sign is used to merge the list.


# use of opertator dunder function in complex number

class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real,"i +",self.img ,"j")

    def __add__(self, num2):
        newReal =self.real + num2.real 
        newImg = self.img + num2.img
        return complex(newReal,newImg)
    

num1 = complex(1,4)
num1.showNumber()

num2 = complex(5,7)
num2.showNumber()

num3 = num1+num2
num3.showNumber()
