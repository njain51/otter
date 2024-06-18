"""
You write a while loop that must not enter into any iteration, as follows:
while(sum([True, True, False, False==False]) == 3):
    print('running...')
You notice infinite iterations when you run the above code, however. What condition satisfies the requirement of stopping the while loop from entering its body?
"""

# answer
# sum([True, True, False==0, False==False]) == 3

"""
In Python, boolean values (True and False) can be treated as integers, where True is equivalent to 1 and False is equivalent to 0.
The sum() function adds these values: 1 + 1 + 1 + 1 = 4
The while loop's condition sum(...) == 3 is now 4 == 3, which is False.
"""