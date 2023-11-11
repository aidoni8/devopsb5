
# Suppose you have a box containing 28 colored 
# pencils,  and you want to divide them evenly 
# among 5 friends so that each friend gets 
# the same number of pencils.

# In order to find number of pencils in each friend
# divide the num of pencils with num of friends.

num_pencils, num_friends = 28, 5

pencil_per_friend = num_pencils / num_friends

print("Each friend will get", pencil_per_friend, "pencils")

left_over_pencils = num_pencils % num_friends

print("I will be left with", left_over_pencils,"num_pencils")