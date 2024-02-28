#Creating the class
# class Student:
#     name= "Rachit Poudel","Sparsha","Rabin"
#     RollNumber = 12,13,14,
#     Address = "Kathmandu",

# #Creatimg the Objects
# s1 = Student()
# print(s1.name)
# print(s1.RollNumber)
# print(s1.Address)

# creating the class
class student:
    collage_name = "Herald Collage Kathmandu." #Class Attributes 
    def __init__(self,name,rollnumber): # this function is called when an object of a class is created
        self.name = name #Instance Attributes.
        self.rollnumber = rollnumber
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