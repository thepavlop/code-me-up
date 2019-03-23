"""
Assignment:
Ask user for an integer N. Return the last multiple of 3, smaller or equal to N.
"""

x = input("Please enter an integer: ")
x = int(x)
my_list = list(range (0, x+1, 3))  # create a list from 0 to N containing only multiples of 3
print('The last multiple of 3 that is smaller or equal to N is:', my_list[-1])
