


list = ['t','e',"c","h","t"]

# What if I want to add a new element to this list? 

# We can use append and insert method. 

# APPEND Method
# Will add element to the end of the list. It takes one 
# argument to be added to end of list. 
print(f"List before append method is {list}")

#Using apppend
list.append(1)
print(f"List after append method is {list}")

#INSERT Method
# This method takes 2 arguments, first argument
# will be the place(index) of second argument in 
# list when it is added.

print(f"List before insert method is {list}")

list.insert(3,"new")
print("Insert method with arguments 3 and new is applied.")
print(f"List after insert method is {list}")

##############################################################################################
##############################################################################################


# Extend Method

# Extend method will add another list to a list that is applied.

l1 = [1,2]
l2 = ["a","b"]
print(f"l1 before extend method {l1}, l2 before extend method {l2}.")

# Apply extend method to l1 with argument l2.
l1.extend(l2)
print("Extend method is applied to l1")
print(f"l1 after extend method {l1}, l2 after extend method {l2}.")

##############################################################################################
##############################################################################################

# Remove and Pop Method

# Remove method will remove the specified `VALUE` from the list, 
# however, Pop method will remove the specified `INDEX` from the list. 

ls = [2,1,5,3,2]
print(f"List before the remove method is {ls}")

ls.remove(2)

print(f"List after the remove method is {ls}")
# Remove method removes first occurence of the given value. 

#POP method. 

ls = [2,1,"str",3,2,[1,2,3]]
print(f"List before the remove method is {ls}")
# ls.pop(10) IndexError: pop index out of range
ls.pop(2)
print(f"List after the pop(2) method is {ls}")

#Note! pop method will return the value it removes from list. 

## Clear method 
# It will remove all elements in list. It empties the list. 

print(f"List before the clear method is {ls}")
ls.clear()
print(f"List after the clear method is {ls}") # []

##############################################################################################
##############################################################################################

#SORT Method
# This will sort the given list in an ascending order. 
# The way that it sorts strings by looking at their 
# ASCII Table values. 
# In the sort method it uses `>` comparison operator. 
# Therefore, if a data types are not compatible to use `>` operator
# this method will generate an error. 




l = [-1, 1,0,True , False, 1.1]

l.sort()
print(l)
print(f"The value of l after the sort method {l}")

l = ["a","z","b","e"]

l.sort()
print(l)
print(f"The value of l after the sort method {l}")















