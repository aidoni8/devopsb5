#Create a simple python program to print if a given string 
# ends with another given string. 
#For that ask this two strings to user.

s1 = input("Enter a string:")
s2 = input("Enter a string:")

#Let's check if the s1 ends with s2

condition = s1.endswith(s2)

# Variable condition will be True if s1 ends with s2,
#it will be False if s1 doesn't end with s2.
# Type opf variable condition is boolean.
print(type(condition)) # <class'bool'>


#Let's also check if s1 starts with s2.

condition2 = s1.startswith(s2)

# Variable condition2 will be True if s1 starts with s2,
#it will be False if s1 doesn't end with s2.
# Type opf variable condition is boolean.
print(type(condition)) # <class'bool'>

print("python".endswith("python")) #True
print("python".startswith("python")) #True

print("python".endswith("pyThon")) #False
#endswith and startswith methods are case sensitive.

print("python".startswith("py")) #True
print("python".endswith("py")) #False


print("python".startswith("p")) #True
print("python".endswith("n")) #False



print("pYthon".startswith("py")) #False

