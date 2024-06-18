lst = [5, True, False, 'Book', 'Integer']
n = sum([1 if i == True else 0 for i in lst])

print(n)  # results in 1

"""
Explanation:

Here's a breakdown of what the code does:

List Creation:

lst = [5, True, False, 'Book', 'Integer'] creates a list containing various elements: an integer, two boolean values (True and False), and two strings.
List Comprehension:

[1 if i == True else 0 for i in lst] is a list comprehension. It iterates through each element i in the list lst and performs the following check:
If i is equal to True, it adds 1 to the resulting list.
Otherwise (if i is not True), it adds 0 to the resulting list.
Sum Calculation:

sum([...]) takes the resulting list from the list comprehension and calculates the sum of its elements.
In Detail:

When the list comprehension iterates over the lst:
For the element 5, the condition i == True is False, so 0 is added.
For the element True, the condition i == True is True, so 1 is added.
For the element False, the condition i == True is False, so 0 is added.
For the strings 'Book' and 'Integer', the condition i == True is False, so 0 is added.
Therefore, the list comprehension creates the list [0, 1, 0, 0, 0].
The sum() function then adds up the elements of this list, resulting in a final value of 1.
"""