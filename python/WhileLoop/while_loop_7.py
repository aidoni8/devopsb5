#Let's print
# Ask user to how many lines of output they would like to see. 
# Our lines should look like
# 1               #THis is the first line and has one number
# 1 2             #This is the second line and has 2 numbers
# 1 2 3           #This is the third line and has 3 numbers
# 1 2 3 4         #This is the 4th line and has 4 numbers
# 1 2 3 4 5       #This is the 5th line and has 5 numbers
# 1 2 3 4 5 6     #This is the 6th line and has 6 numbers
# 1 2 3 4 5 6 7   #This is the 7th line and has 7 numbers


line_limit = int(input("Enter a number of lines you would like to see."))
line_number = 1
while line_limit >0:
    print(line_limit)
    line_limit -= 1


line_limit = int(input("Enter a number of lines you would like to see."))
line_number = 1
while line_number <= line_limit:
    print()
    #I have to execute to loop that repeats line_number times.
    numbers_in_line = 1
    while numbers_in_line <= line_number:
        print(numbers_in_line, end="")
        numbers_in_line += 1

    line_number +=1




