
num = 11

# How can I learn the type of this variable?
print("Type of the variable num is", type(num))
print("The value of the varibale num is", num)

num = 11

# How can I learn the type of this variable? 
print("Type of the variable num is",type(num))
print("The value of the variable num is", num)

num += 30
print("Type of the variable num is",type(num)) # int
print("The value of the variable num is", num) # 41

num *= 2
print("Type of the variable num is",type(num)) # int
print("The value of the variable num is", num) # 82

num /= 2
print("Type of the variable num is",type(num)) # float
print("The value of the variable num is", num) # 41.0

num **= 1
print("Type of the variable num is",type(num)) # float
print("The value of the variable num is", num) # 41.0

num %= 8
print("Type of the variable num is",type(num)) # float
print("The value of the variable num is", num) # 1.0

num //= 1
print("Type of the variable num is",type(num)) # float
print("The value of the variable num is", num) # 1.0

# Note! Once the type goes to float using any ARITHMETIC
# operation will not change the type to integer.

num = 1
print("Type of the variable num is",type(num)) # int
print("The value of the variable num is", num) # 1