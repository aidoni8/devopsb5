
# In order to store multiple objects in a single variable,
# we can use list type. List is 1 of 4 built-in collection 
# type in python. 
# List is an iterable, ordered and mutable object.

# create a list

ls = ['str', 7, 5.3, True]

print(type(ls)) # <class 'list'>

# We can access the elements of lists using index numbers. 

# Access the third element from the list. (Index 2)
item = ls[2]

print(f"Type of variable item is {type(item)} and the value of item is {item}")

# List also has negative indexing. 

print(ls[-1])


# ls = ['str', 7, 5.3, True]

# Getting the range of elements from list. 
# This implementation would work similarly to slicing 
# in string. 

items = ls[1:4]

print(f"Type of variable items is {type(items)} and the value of items is {items}")

# After slicing a list, we get another list. 



# ls = ['str', 7, 5.3, True]

for elm in ls:
    print(elm)

















