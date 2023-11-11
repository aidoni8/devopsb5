#Write a program that will accept 5 digit number and
#will print reversed number at the end.
#Example-1:
#53876
#The output is 67835
#Example-2:
#97352
#The output is 25379

five_digit_num = 76543

print(last_digit) 
four_digit_version = five_digit_num // 10

fourth_digit = four_digit_version % 10
print(fourth_digit)
three_digit_version = four_digit_version // 10

third_digit = three_digit_version % 10
print(third_digit)
two_digit_version = three_digit_version // 10

second_digit = two_digit_version % 10
print(second_digit)

first_digit = two_digit_version // 10
print(first_digit)
last_digit = five_digit_num % 10