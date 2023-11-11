four_digit_num = 9876
# Create a program that will find each digit just using
# the variable name.
# One fact is that number is always going to be 4 digit.

# 32  % 10 -> 2
# 49  % 10 -> 9
# 101 % 10 -> 1
# 217 % 10 -> 7
# 8   % 10 -> 8
# 93  % 10 -> 3
#NOTE! Every time finding a remainder with 10 gives us
# last digit from the number.

# 32  // 10 -> 3
# 496 // 10 -> 49
# 101 // 10 -> 10
# 217 // 10 -> 21
# 8   // 10 -> 0
# 93  // 10 -> 9
#NOTE! Every time a number is divided by 10 will
# lose its last digit.

# 9876 % 10 -> 987.6
# 987.6 % 10 -> 98.76
# 98.76 % 10 -> 9.876
# 9.876 % 10 -> 0.9876

# Find the remainder with 10 which will give last digit
# since the last digit is found then remove it by dividing
# 10
four_digit_num = 8765

print(last_digit)
three_digit_version = four_digit_num //10

third_digit = three_digit_version % 10 
print(third_digit)
two_digit_version = three_digit_version // 10

second_digit = two_digit_version % 10
print(second_digit)

first_digit = two_digit_version // 10
print(first_digit)
last_digit = four_digit_num % 10