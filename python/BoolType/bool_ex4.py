# We should create a program to calculate if there is still a ticket
# for the game tonight. We are given two variables: Capacity of the stadium.
#and the amount of tickets sold.
#Print True if I can stilll buy a ticket, False otherwise.
# Note! User will enter the capacity and amount of tickets sold.

stadium_capacity = input ("Please enter the stadium capacity:")

sold_tickets = int(input("Please enter the amount of tickets sold:"))

# How can I check if there is still a space?

is_there_space = stadium_capacity > sold_tickets

print("There is space for the game tonight:", is_there_space)