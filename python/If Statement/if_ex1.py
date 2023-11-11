# Ask user to enter twwo equal integer variables,
# if user enters two numbers that are same we will print 'You entered two equal numbers.'. If user enters two different numbers,
#we will print 'You don't follow the instructions'.
print("Enter two numbers below that are equal.")
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))


if num1 == num2:
  print("You entered two equal numbers.")
elif num1 != num2:
  print("You don't follow the instructions")

# Note! By using elif statement we are telling python that both conditions
# can't be True, so If the first condition is YTrue, it doesn't check the
# elif's condition.
# We could say that we use elif statement for conditions that depend on
# each other so either one or the other one is True.







