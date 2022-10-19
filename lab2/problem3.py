# Problem 3
# Given two strings, return True if either of the strings
# appears at the very end of the other string, ignoring 
# upper/lower case differences (in other words, the computation should not be 
# "case sensitive"). Note: s.lower() returns the lowercase version of a string. 
# Examples: end_other('Hiabc', 'abc') → True end_other('AbC', 'HiaBc') → True end_other('abc', 'abXabc') → True

def end_other(s1,s2):
  s1 = s1.lower()
  s2 = s2.lower()
  if len(s1) <= len(s2):
    return  print('\'s1\' in \'s2\' -> {}'.format(s1 in s2))
  else :
    return print('\'s1\' in \'s2\' -> {}'.format(s2 in s1))
end_other('Hiabc', 'abc')
end_other('AbC', 'HiaBc')