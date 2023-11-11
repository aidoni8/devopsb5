# Mulitiple of 3 and 5
#Write a program that makes a number as input and prints
# True if the number is a multiple of both 3 and 5, False otherwise.
# Note: Multiple of 3 and 5 means that it could be divisible by both 3 and 5.

number = int(input("Enter a number:"))
# If a number is divisible by another number there should not be a remainder.
is_divisible_3 = number % 3 == 0
is_divisible_5 = number % 5 == 0

print(is_divisible_3 and is_divisible_5)
# result = number % 3 == 0 and number % 5 == 0
#print(result) 


