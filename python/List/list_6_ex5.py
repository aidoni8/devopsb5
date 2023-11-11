# split() method in string
# split method takes one argument as a separator, and separates 
# string on that argument and stores in a list. 

str = "Weather is not that good today."

ls = str.split(" ")

print(ls)

ls = str.split("a")
print(ls)

# Given a sentence find out all the words that starts with upper case. 

sentence = "Python is Platform Independent programming Language."

# I can create a list using split method that contains all the words. 
words = sentence.split(" ")
#Let's look at each word from the list of words.
capitalized_words = []
for word in words: 
    #Let's get the first character of word
    f_ch = word[0]
    if f_ch.isupper():
        capitalized_words.append(word)

print(capitalized_words)














