age = 23
age = age + 1

print(age)

#checking age datatype
print(type(age))

#it will not work because age is a integer and you
#want to add int data type in a string datatype
#so the solution is to make the integer variable into string

#print("Your age is " + age)

print("Your age is:" + str(age))