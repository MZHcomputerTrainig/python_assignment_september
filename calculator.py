#Calculator Program
#Programmer : Tr Autumn

firstnum = int(input("Enter first value"))
secondnum = int(input("Enter second value"))
operator = input("Operator (+ - * /)")
try:

    output = True

    if operator == "+":
        result = firstnum + secondnum

    elif operator == "-":
        result = firstnum - secondnum


    elif operator == "*":
        result = firstnum * secondnum


    elif operator == "/":
        result = firstnum / secondnum

    else :
        output = False
        print("Wrong Operator ")

    if output:
        print("Result is", result)

except ValueError:
    print("Please enter number only")
    print(ValueError)
