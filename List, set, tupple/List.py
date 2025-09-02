# List = [] ordered and changeable. Duplicates ok
fruits = ["apple", "orange", "banana", "coconat"]

print(fruits[0])
print(fruits[:]) #prints all
print(fruits[:3]) #prints first 3 value
print(fruits[2:]) #prints last 2
print(fruits[::2]) #print apple banana (skip)
print(fruits[::-1]) #prints backwords
print(fruits[::3]) #prints apple coconat (if 2 skip 1 , if 3 skip 2)

print(len(fruits))
print("apple" in fruits) #find is apple in fruit or not
fruits[0] = "pinapple" #replace apple into pinapple
fruits.append("Lichi")
# fruits.remove("apple")
fruits.insert(0,"apple") #insert in a position
fruits.sort() #sort in ascending order
fruits.reverse() #reverse 
fruits.clear() #clear every data in fruits
fruits.index("apple") # find index of apple
fruits.count("banana") #count how many time banana in fruits

for x in fruits:
    print(x)

# print(help(fruits)) #find everything in fruits 
# print(dir(fruits))

mixed = [1, "hello", 3.5, True]
print(mixed[-1])