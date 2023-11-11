# Ask user to enter a string with two words. 
# Find first word and last word. 
# Find last letter of first word, find first letter of second word. 
# IF USER enters more than two words print invalid entry. 
#

words = input("Enter a string with two words: ").strip()

# How many spaces do you expect in a string with two words? 
# 1
# How can I find the number of spaces in given string? 
# A:using count method with space argument. 
#How can I remove the leading and trailing spaces? 
# A: to remove leading and trailing space I can use strip() method. 
# Where do you think the first word ends in the string? 
# A: Ends right before the space
# How can I find the index of space? 
# A: using find method with space string argument. 
# How can I get the first word? 
# A: by slicing from index 0 to index_of_space
# How can I get the second word? 
# A: by slicing from index_of_space + 1
# techtorial academy
count_of_spaces = words.count(" ")

if count_of_spaces == 1:
    print("You entered two words")
    index_of_space = words.find(" ")
    first_word = words[0:index_of_space]
    second_word = words[index_of_space+1:]
    print(first_word)
    print(second_word)
    print(f"last letter of first word is {first_word[-1]}")
    print(f"first letter of second word is {second_word[0]}")

else:
    print("Invalid entry")
























