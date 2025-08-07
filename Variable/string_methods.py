first_name = "rafat"
last_name = "GAZI"

#print length of a string (indexing will be 1,2,3,4)
print(len(first_name))

#find where "a" is.. (indexing will be 0,1,2,3...)
print(first_name.find("a"))

#1st word will be capitalized
print(first_name.capitalize())

#all word will be in upper case
print(first_name.upper())

#all word will be in lower case
print(last_name.lower())

#is degit?
print(last_name.isdigit())

#is alphabetical char? if there is a space it will print false.. true if only letters
print(last_name.isalpha())

#count how many time this letter in the variable
print(first_name.count("a"))

#replace a word to another word
print(first_name.replace("a" , "k"))

#print multiple time
temp = first_name + " "
print(temp * 5)