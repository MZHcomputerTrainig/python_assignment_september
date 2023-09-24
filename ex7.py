#7. Write a Python program that accepts a filename from the user and prints the extension of the file.


filename = input("Input the file name:")

fextns = filename.split(".")

print ("The extension of the file is:" + repr(fextns[-1]))