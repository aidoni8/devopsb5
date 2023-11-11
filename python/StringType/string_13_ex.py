# Given a string, if the first or last chars are 'z', 
# print the string without those 'z' chars, and
#  otherwise print the string unchanged.

# "zHiz" → "Hi"
# "zHi" → "Hi"
# "Hziz" → "Hzi"
# "zzHizz" → zHiz


s = input("Enter a string:")

s = s.removeprefix("z")
s = s. removesuffix("z")
print(s)

















