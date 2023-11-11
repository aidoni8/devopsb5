
# Ask user to enter a password but there will be conditions.
# our condition for a valid password is:
#1. it has to have an upper case
#2. it has to have a lower case
#If user provides a valid password print 'your password is valid
#Otherwise, print 'your passsword is not valid'.

user_pass = input("Enter a pass.with an upper and lower case:")

#if user _pass equals to user_pass.lower()What do you think?
# A: it would mean og.consists of all lower cases.
#if user _pass equals to user_pass.upper()What do you think?
# A: it would mean og.consists of all upper cases.
# do we want any one of situation above to be true?
# A: We don't want both of situations above to be false at the
#same time.


b1 = user_pass != user_pass.lower() #this would have meant that string is all lower case.
b2 = user_pass != user_pass.upper()#this would have meant that string is all upper case.

if b1 and b2:
    print("your password is valid")
else:
    print("your password is NOT valid")



c1 = not user_pass.islower()
#c1 will be True if all the letters in user_pass is lower case.
#c1 will be False if user_pass is not in All lower case.

c2 = not user_pass.isupper()
#c2 will be True if all the letters in user_pass is upper case.
#c2 will be False if user_pass is not in All upper case.

#1. it has to have an upper case
#2. it has to have a lower case



if c1 and c2: 
    print("your password is valid")
else:
    print("your password is NOT valid")


print("Tec".lower()) #tec
print("Tec".islower()) #False
print("Tec".isupper()) #False

