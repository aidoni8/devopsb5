#  Leap Year
# A year is leap if it is divisible by 4 but not by 100 
# unless it is also divisible by 400. 
# Write a program that takes a year as input 
# and prints True if it's a leap year, False otherwise.
# 2000, 2024, 2020, 1916, 400 ...



year = int(input("Enter the year that you want to learn if it is a leap yesr:"))

#What conditions should this year give me so that I know it is a leap year/
#I am looking a for a year number that is divisible by 4 but not 100.
# Or it could be divisible by only 400 and it is a leap year.

is_leap = year % 4 ==0 and year % 100 != 0 or year % 400 == 0 

print("Is the given year leap?", is_leap)
# Note if the number x is divisible by number z its means
# x % z == 0 evaluates to true.
# if x % z == 0 is true it means x is divisible by z.









