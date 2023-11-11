# You're given a list of product reviews. Each review is represented 
# as a list with a username, product ID, and a star rating (from 1 to 5).
# Your task is to write a Python program that identifies products with an 
# average rating below 3 and lists the usernames of those who reviewed them.
#Assume each review entry is a list of the form 
#(username, product_id, star_rating).
reviews = [    
    ["JohnD", "P123", 4],
    ["AliceS", "P124", 2],
    ["BobM", "P123", 5],
    ["EveN", "P125", 1],
    ["CarolT", "P124", 2],
    ["DaveL", "P126", 3],
    ["EveN", "P124", 3]
]
#Output
# [["P124",["AliceS","CarolT","EveN"]],["P125",["EveN"]]]

products = []# I am going to add product id in this list if a product 
# has less than 3 rating.
end_list = []

# We have to check each review
for item in reviews:
    # Type of item? -> list
    username, product_id, rating = item 
    if product_id not in products:
        count = 0
        total_rating = 0
        users = []
        for item in reviews:
            if product_id == item[1]:
                count+=1
                total_rating += item[2]
                users.append(item[0])
        if total_rating / count < 3:
            products.append(product_id)
            product_user = [product_id,users] 
            end_list.append(product_user)       


        



print(end_list) # We want to see products less than 3 average rating
















