#Strings all usefull methods cheatsheet

deep = "djCodes"

print(len(deep)) #To Find the length of string

print(deep[3]) #Strings are character arrays you can print values by giving index number

print(deep[2:5]) #You can print particular elements by giving a starting and ending index (last index not included)

print(deep[-4:-2]) #You can reverse a string by negative indexing (note -ve indexing starts from -1 in py)

print(deep.strip()) #Removed Whitespaces from string

print(deep.upper()) #Returns String in Upper character

print(deep.lower()) # Returns string in lower character

print(deep.capitalize()) #To Make 1st letter capital

print(deep.casefold()) #To make all letters small

print(deep.count("C",0,5)) # To count the number of occurance of a character/characters

encoded = deep.encode()
print(encoded) #To encode a String

print(deep.endswith("s",0,7)) #WTo check weather a strings ends with particular character (Returns Bool)

print(deep.find("d",0,7)) #Returns theindex position of the element

print(deep.replace("d","D")) #Replaces character

dj = "27"
print(deep+dj) #To concate 2 springs


