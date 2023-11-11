# Given a list of elements, print only 
# int values from the list.

l = [1,True,"False",7,"str","t",[1,2,3],{},"10","11"]

# Let's access the all elements first.

for item in l:
    #Let's print the type of each element in the list. 
    if str(type(item)) == "<class 'int'>":
        print(item)
    # We need to make sure the type is <class 'int'>

print(l[2][0].lower()) # f
# I want to access second element in the list which is stored 
# in variable `l`
print(l[6][1]) # it prints 2
print(l[-1][0]) # it prints 1








