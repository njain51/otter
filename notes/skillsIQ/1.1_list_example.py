# You have two lists as follows: You must concatenate the values to these lists to output a tuple ('Hello,',
# 'there!', 'How', 'are', 'you', 'doing?'). How would you write its code?
list1 = ['Hello,', 'How', 'you']
list2 = ['there!', 'are', 'doing?']

# The zip() function returns a zip object, This creates an iterator of tuples, pairing corresponding elements from
# list1 and list2:
print(zip(list1, list2))

# convert to list, This converts the iterator into a list of tuples:
print(list(zip(list1, list2)))

# The sum() function is typically used for adding numbers.  However, you can provide a "start" value as the second argument. By starting with an empty tuple (), the sum function effectively concatenates the tuples in the list:
# print(sum(list(zip(list1, list2))), ())
print(sum(list(zip(list1, list2)), ()))



print('Hello World')
