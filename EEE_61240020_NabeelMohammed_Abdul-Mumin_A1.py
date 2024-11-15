import numpy as np
import math  #Declaration of math module

#QUESTION 1.Mathematical Function
# numpy is a mathematical modules used in calculation in python
#i used log instead of In because we dont have In in python
def calculate_f(x,y,z):
    result = (np.sin(2*x)**2 + np.exp(y**2) * np.log(z+1))/np.sqrt(x**2 + y**2 + z**2 + 2)
    return result
# we use round() to get the number of decimal place you want it takes two arugments the i.e round(result,decimal)
print(calculate_f(1,0.5,2),3)







#QUESTION 2 creating function:
    #TASK1:
a = int(input("Enter a number for a:\n"))
b = int(input("Enter a number for b:\n"))
def hypotenuse():
    c = np.sqrt(a**2 + b**2)
    return c
# I used f string here
print(f"The hypotenuse of c is { hypotenuse()}")
    
    #TASK2
def firstargument(first,second):
    # since we want an output or result of 652 we need to go with this calculation
        return first*second**2 + first + 2
print(firstargument(25,5))
def secondargument(word,number):
    # output of this function should be word 4 times eg.PYTHONPYTHONPYTHONPYTHON:
        return str(word)*number*2
print(secondargument("PYHTON",2))
    
    #TASK3
    #inputs statement   
x1 = int(input('Enter a number for x1:\n'))
y1 = int(input('Enter a number for y1:\n'))
x2 = int(input('Enter a number for x2:\n'))
y2 = int(input('Enter a number for y2:\n'))
def distance(x1,y1,x2,y2):
        calculated_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return calculated_distance
print(distance(x1, y1, x2, y2))
    
    #TASK4
def twice(argument):
    return argument*2
result = twice(10)
print(f"Argument is printed twice {result}")
def concatenate_twice(first, second):
    result = str(first) + str(second)
    return result
result =  concatenate_twice("Nabeel", "Mohammed")
print(result)

    #Task5
def percentage(num1,num2):
    cal_percentage = (num1/100)*num2
    print(f"{num1}% of {num2} is {int(cal_percentage)}")
percentage(20, 100)
percentage(200, 50)

    #TASK 6
name = input("Enter your name\n")
surname = input("Enter your surname\n")
department = input("Enter your department\n").upper()
student_ID = int(input("Enter your student ID\n"))
email = input("Enter your email address\n")
phone_number = int(input("Enter your phone number\n"))
def information(name,surname,department,student_ID,email,phone_number):
    result = f"Name & Surname: {name} {surname}\nDepartment & Student ID: {department} {student_ID}\nEmail: {email}\nPhone Number: {phone_number}"
    return result
result = information(name, surname, department, student_ID, email, phone_number)

print(result)









#QUESTION 3 MULTIPLICATION
first_num = int(input("Enter a first number\n"))
second_num = int(input("Enter a second number\n"))
def multiply(first_num,second_num,row = 1):
    # we need a row here because we need to calculate from 1 to 10 and when the row gets to 10 its going to return back to the code
    # and if there are no other options it stop there
    if row > 10:
        return
    print(f"{first_num} X {row} = {first_num * row}  \t{second_num} X {row} = {second_num * row}")
    #\t it used to create a seperate table 
    multiply(first_num, second_num,row + 1)
# why row + 1... so it added up eg if row = 1 , row = 1 + 1=2....
multiply(first_num, second_num)