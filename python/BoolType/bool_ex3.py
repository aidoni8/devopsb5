# We are given three sides of a triangle.
# Triangle is equilateral when all sides are the same.
# So in this code we have to display True when triangle is equilateral,
# False otherwise.

a = 9
b = 9
c = 10

is_equilateral = a == b == c
# the calculation above is possible 
# because Python supports
# chained comparison operator.
print (is_equilateral)