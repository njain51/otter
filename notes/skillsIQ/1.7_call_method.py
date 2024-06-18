"""
The __call__ method is the special method that needs to be defined to make an object callable in Python.

When you define __call__ in a class, you can then use instances of that class as if they were functions, calling them with parentheses and passing arguments.
"""


class MyCallable:
    def __call__(self, x):
        return x * 2


obj = MyCallable()
result = obj(5)  # Calls the __call__ method
print(result)  # Output: 10
