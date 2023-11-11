a = b = c = d = 5

#These varaiables are not dependent on each other.
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
a, b, c, d = 4, "3", 2.0 , 1 + 1j 
print("After reassignment")
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

#Python always looks for the last assignment to the line
#it is executing.

