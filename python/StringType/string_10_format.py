#Formatting is sort of a short cut to embed values from other
#data types in to string.

#There is two ways we could fromat strings.
#*1 using fromat method.
#Ex: We will put curly braces in a string,
# and those curly braces will be replaced by an argument
#that we put in format method.

s = "Today weather is {} fahrenheit."
print(s) # Today weather is fahrenheit.

print(s.format(84))
print(s.format("eighty four"))

#Note! We could use more than one curly brace to format
#strings, as well as using index for curly braces.
age =int(input("Enter your age"))
name =input("Enter your name")
s2 = "My name is {} and my age is {}."
print(s2) #My name is {} and my age is {}

print(s2.format(name,age))

s3 = "The brand of the laptop is {1}, and model year is {0}:"

print(s3.format(2019, "Linux"))


#Second way to format strings is using f-strings.
#We still use curly braces but this time we add
#the name of variables inside the curly braces.
fahr = 84
s = f"Today weather is {fahr} fahrenheit."
print(s) #Today weather is 84 fahrenheit.










