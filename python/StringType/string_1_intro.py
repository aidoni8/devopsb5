# Ask user to enter a string
#print the length of the given string, and print the
#5th letter from string.

s = input(" Enter anythin: ")

# What is the lenght for this string?
print(len(s)) 

#Which index number we should find in string?
#I need to find the letter at index 4
print(s[4]) #this will bring the 5th character in string.


##what would be the last(biggest) index number in string above?
biggest_index =len(s) - 1
if biggest_index >= 4:
    print(s[4])
else: 
    print("Sorry but there is no index 4 in string.")
    
# Refactor this code so that it would not generate an error when
#user enters a string that does not have index 4.














#Note! If the index number we are trying to access doesn't 
# exist in string, it will generate IndexError.









