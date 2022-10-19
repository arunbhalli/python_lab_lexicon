# Problem 2
# Given a string, return a new string made of every other
# character starting with the first, so "Hello" yields "Hlo".
# For example:
# stringBits('Hello') → 'Hlo' stringBits('Hi') → 
# 'H' stringBits('Heeololeo') → 'Hello'






def stringbits(strValue):
  strValue = strValue[::2]
  return print(strValue)
stringbits('Hello')
stringbits('Heeololeo')