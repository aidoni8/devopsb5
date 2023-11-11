# Create a program that asks a user an integer value.
# if this integer value is even double the number and print out the result.
# if the number is odd print (You enetered an odd number.)

number = int(input("Please enter an integer value:"))

# We should check if the given number is odd or even.
# Can these two conditions be True at the same time?
# No, because either one of them can be Trye only:
if number % 2 == 0:
   print(number * 2)
elif number % 2 != 0:
   print("You entered an odd number.")