# Problem 4
# Given a string,
# return a string where for every char in the original,
# there are two chars.
# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'


def doubleChar(str):
    return print("".join([x*2 for x in str]))
doubleChar('The')
doubleChar('AAbb')
doubleChar('Hi-There')
