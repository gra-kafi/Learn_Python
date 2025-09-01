# set = {} unordered and immutable, but add/remove ok. No duplicates
# we can use set for constant 
fruits = {"apple", "banana", "coconat", "orange"}

print(fruits) #change index every time
print(len(fruits))
print("apple" in fruits)
#print(fruits[1]) #index won't work
fruits.add("pinapple")
fruits.remove("apple")
print(fruits)
fruits.pop() #will remove whatever in the fast but it will be random
print(fruits)
