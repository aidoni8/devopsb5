# In the factory we need to create a program that can 
# find if we can do the shipment and, if we can do the shipment
# it will tell us how many small package we should ship.
# First we need to get total kilogram of the shipment,
# to reach this total kilogram of shipment we can use small and big packages. 
# Every big package is 5 kilogram and every small packages is 1 kilogram.
# We have limited amount of small and big packages. 
# Ask user how many big and how many small package  they have.
# Ask user what is the total goal kilogram of the shipment.
# Print whether they can ship, if they can ship print how many small packages they need. 
# Assume big packages is used before small packages.

total_goal_shipment = int(input("Enter the amount of shipment in kg:"))
#In order to reach the number above I need to combine number of small
# packeges and number of big packages.
small_pack = int(input("Enter the small packeges in inventory:"))
big_pack = int(input("Enter the big packeges in inventory:"))

#A small packages weighs a kg, and a big package weighs 5 kg.

# I need to ship 34 kg, i have 10 big packages and no small packages.
# I need to ship 29 kg I have 4 big packages and 9 small packages?

#In first situation i had enough amount big packages however i didn't have
# the necessary small packages.

ideal_needed_big_package = total_goal_shipment // 5

if big_pack >= ideal_needed_big_package:
    ideal_small_pack_needed = total_goal_shipment % 5
    if small_pack >= ideal_small_pack_needed:
        print ("We can ship and I need to use",ideal_small_pack_needed,"amount of small package.")
    else:
        print( "We can't do shipment because we don't have enough small package.")
elif big_pack < ideal_needed_big_package:
    # Use all the big packages
    total_amount_from_big_pack = big_pack * 5
    small_pack_needed = total_goal_shipment - total_amount_from_big_pack
    if small_pack_needed <= small_pack:
        print("I can do the shipment:")
    else: 
        print("I cannot do the shipment because we didn't have ideal big packs.")