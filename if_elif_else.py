#Get user input for name and password
name = input("Enter your name:")
password = input("Enter your password")
#Check the name and password
if name=="admin" and password== "password":
    print("Welcome, admin! ")
elif name=="guest" and password=="guestpass":
    print("Welcome, guest!")
else:
    print("Invalid name or password. Access denied.")