#when we recive a input it will be always a string data type



x = input()
print("hi " + x)

y = input("Enter your age: ")
print("your are " + y + " years old")

# it will not work because this is a string
#print(y+1)

y = int(y)
print(y+1)

#or we can make it int when we take input

z = int(input("What year is this?"))

z = z+1
#you cannot display a int in a string
print("next year " + str(z))
print(z)

height = float(input("How tall you are?"))
print("you are "+str(height)+" feet")