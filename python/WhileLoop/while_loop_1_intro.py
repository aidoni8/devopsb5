
#Let's create a loop to print numbers from 1 to 5.
#We have to be doing something that would eventually change the condition.

num = 1
while num <= 5:
    print(num)
    num += 1

print(f"Value of the vraiable num after the loop is {num}")


#Let's create a program that will print all numbers from 20 to 1 inclusive.

num = 20
while num > 0:
    print(num)
    num -= 1 #this means num = num -1 


#Let's create a program that will print numbers from 1 to 10
#for even numbers it will say 'number is even",
#for odd numbers it will say 'num is odd'

num = 1
while num <=10:
    if num % 2 == 0 :
        print(f"{num} is even number.")
    else:
        print(f"{num} is odd number.")
    num +=1

