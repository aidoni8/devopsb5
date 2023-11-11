# Logical Operators in Python

## and operator
- 'and' operators checks if **all** conditions are true. For ex:
''' py
# Let's write a program to see if a person can drive:
# In order to drive they must be over 15 years old and they must have a
# valid license
age = 18
has_license = True
can_driven = has_license and age > 15

'''

## or operator
- 'or' operator checks if at least one condition is True. For ex:
'''py
# A worker can get rest when it is weekend or when it is on holidays.
is_holiday = True
is_weekend = False
can_rest = is_holiday or is_weekend
'''

## not operator
- Recerses the result of a bollean variable. For ex:
''' py
b1 = True
b1 = not b1
print(b1) # False
b1 = not b1
print(b1) #True 

'''

''' py 
print(True and not False) # True
print(not True and True) #False 
print(True and True and True and False ) #False
print(True or False) # True 
print(not False or False) #True
print(False or False) #False
print(False and False) #False

# Using both 'and' and 'or' operator at the same time.
# In python 'and' operator will be executed before the 'or' operator.
print (False or True and False) #False
# NOTE: not operator will be executed before the 'and' and 'or' oprators.

'''

#Immutability 
- All numerical data types in python are immutable which means
their value will not be modified in any case other than reassignment. 

