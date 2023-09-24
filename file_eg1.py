#file create and write

f = open("demofile1.txt","w")

f.write("I like coffee")

f.close()

# open and read the file 

f= open ("demofile1.txt","r")
print(f.read(5))
f.close()

f= open ("demofile1.txt","r")
print(f.readline())
f.close()


f= open ("demofile1.txt","r")
for str in f:
    print(str)
f.close()



f= open ("demofile1.txt","r")
print(f.readlines())
f.close()
