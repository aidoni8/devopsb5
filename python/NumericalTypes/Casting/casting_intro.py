# In python we can also convert data types to each other
# using constructor function of that specific type.

var1 = 5.1
print(type(var1)) # <class 'float'>

# class is the file that makes
# the data structure.

var1 = 5.9
print(type(var1)) # <class 'float'>
print(var1) # 5.9
var1 = int(var1) #making integer just removes the decimal point
print(type(var1)) # <class 'int'>
print(var1) # 5
var1 = float(var1)
print(type(var1)) # <class 'float'>
print(var1) # 5.0