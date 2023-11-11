

# removeprefix method will take one string argument, 
# and it will remove argument from the string if the 
# string starts with argument. 

email = "yct@techtorialacademy.com"

print (email.removeprefix("techtorial"))#yct@techtorialacademy.com
# since the string doesn't start with techtorial it won't remove.

print(email.removeprefix("yct")) # @techtorialacademy.com

# removesuffix method will take one string argument, 
# and it will remove argument from the string if the 
# string ends with argument. 
print(email.removesuffix("yc")) #yct@techtorialacademy.com 

print(email.removesuffix(".com"))# yct@techtorialacademy

# What is the return type of removesuffix and removeprefix method? 
# it will return a new string value. 

print(email) #yct@techtorialacademy.com








