
#Finding if a string contains another string.
#We can use in operator

s = "tectorial"
if "t" in s:
    print ("This line will be executed because string s contains t.")



#Create a program, and ask user to enter a string.
# From the input string print only vowel letters. (vowel are a, e, u, i, o)
s = input("Enter a string:").lower()
# Create a string that has all vowels in it.
vowels = "aeuio"

#I will create a loop to go through each letter in string.
index = 0
while index < len(s):
    #Here after getting the letter, I have to check if the current letter
    #is vowel
    if s[index] in vowels:
        print(f"Letter {s[index]} in string is vowel.")
    index += 1












