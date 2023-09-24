#Python program for simple calculator
# By Tr Autumn

#function to add two numbers

def add(num1, num2):
    return num1 + num2

#function to subtract two numbers

def sub(num1, num2):
    return num1 - num2

#function to multiply two numbers

def mul(num1, num2):
    return num1 * num2


#function to divide two numbers

def div(num1, num2):
    return num1 / num2

print("Please select operation - \n"\
      "1.Add\n"\
        "2.Subtract\n"\
            "3.Multiply\n"\
                "4.Divide\n")

#Take input from the user

select = int(input("Select operations from 1,2,3,4:"))

num1 = int(input("Enter first Number:"))
num2 = int(input("Enter second Number:"))

if select == 1:
    print(num1,"+",num2,"=", add(num1,num2) )

elif select == 2:
     print(num1,"-",num2,"=", sub(num1,num2) )

elif select == 3:
     print(num1,"*",num2,"=", mul(num1,num2) )

elif select == 4:
     print(num1,"/",num2,"=", div(num1,num2) )

else:
    print("invalid input")