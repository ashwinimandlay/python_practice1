# text alignment
# In Python, a string of text can be aligned left,
# right and center.

# left alignment-->'string'.ljust(width, fill character = '-')
# if fillcharacter is not specified then
# by default it is space
print('HackerRank'.ljust(20, '-'))

# note : width here is total width including string
# if width is less than string then there will be no fill
# character ex:

print('HackerRank'.ljust(4, '-'))


# similarly:
# .center(width, fillcharac)
# .rjust(width, fillcharac)
