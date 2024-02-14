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

#creating the class
class student:
    def __init__(self,name,rollnumber): # this function is called when an object of a class is created
        self.name = name
        self.rollnumber = rollnumber


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
print("\n\n The Details of ",s2.name," are as follows : ")
print("Name : ",s2.name)
print("Roll Number : ",s2.rollnumber)
