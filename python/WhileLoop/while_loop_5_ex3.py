#Given a string from user, print the mirror ends.
#abchfjuhfcba -> abc
#hannah -> hannah
#civic -> civie
#atechtoriala -> a
str = input("Enter a string:")

l_to_r = 0 #left to right index
r_to_l = -1 # right to left index

#left to right index should keep getting bigger,
# right to left index should keep getting smaller.
mirror_end = ""
while l_to_r < len(str):
    #How can I check if the letters for these indexes are matching?
    if str[l_to_r] == str[r_to_l]:
        mirror_end += str[l_to_r] # you could also assing to r_to_l since they 
    else:
        break

    l_to_r += 1
    r_to_l -= 1 

print(mirror_end)





