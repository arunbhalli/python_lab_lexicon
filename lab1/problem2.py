'''Problem 2:
Given this nested list:my_list = [3,7,[1,4,'hello']]
Reassign "hello to be "goodbye"'''


my_list = [3, 7, [1, 4, 'hello']]
my_list[-1][-1] = 'goodbye'
print(my_list)
