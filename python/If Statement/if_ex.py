# Create program that calculates the grade letter of a student.
# Ask user their grade as an integer number.
#Print 'Not a valid grade' if the grade is lower than 0 or bigger than 100.
# Print A+ if the grade is higher than 94
# Print A if the grade is in betwenn 85 and 94 inclusive.
# Print B if the grade is in between 75 and 84 inclusive.
# Print C if the grade is between 65 and 74 inclusive.
# Print grade doesn't meet expectations when the grade is lower than 65.



# How many conditions are we going to cover?
# 6
# Do these conditions depend on each other?
# Yes, they do.
# We are going to use elif condition.

grade = int(input("Enter your grade as an integer:"))
if grade > 100 or grade < 0:
    print ("Invalid grade.")
elif grade > 94:
    print("A+")
elif 85 <= grade <=94: #   85 <= grade <=94 translates to 85 <= grade and grade <=94
    print("A")
elif 75 <= grade <=84:
    print("B")
elif 65 <= grade <=74:
    print("C")
elif grade < 65:
    print("Grade doesn't meet expectations.")