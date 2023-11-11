
#find method will return us the lowest index of a given charachter
#or sequence of characters.

s = "Techtorial Academy"

print(s.find("a")) #8
print(type(s.find("a"))) # <class'int'>

print(s.find("b")) # -1
print(type(s.find("b"))) #<class 'int'>

print(s.find("de")) #14
# When it is given sequence of characters it will return where that
#sequence starts in string.


print(s.find("ac")) #-1
# "Ac" is never same as "ac"
#There is no sequence "ac" in string

print(s.find("Tectorial")) #0
# When it is given sequence of characters it will return where that
#sequence starts in string.


#Get Techtorial from string s.
print(s[:10]) #type of slicing is string.












