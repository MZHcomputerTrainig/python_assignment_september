from random import randint
def write():
    #Open file for wirting data

    f = open("numberfile.txt",'w')

    for i in range(10):
        f.write(str(randint(0,9)) + "")
#close the file
    f.close()
#write() #Call the write function



def read_file():
    filename = input("Enter File name:")
    infile = open(filename, "r")
    s = infile.read()
    numbers = [eval(x) for x in s.split()]  # number list
    for number in numbers:
        print(number, end="")
    infile.close()

read_file()



