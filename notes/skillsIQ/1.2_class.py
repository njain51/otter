
# How can you ensure that no method overriding takes place in the code?

class ClassA:
    def r(self):
        pass


class ClassB(ClassA):
    def r(self):
        pass


"""In Python, method names that start with a double underscore (__) are considered private or "dunder" methods. These
methods are not directly accessible from outside the class and are not part of the normal inheritance mechanism. By
renaming the method r to __r in both classes, you make it a private method. This means that the __r method in ClassB
will not override the __r method in ClassA. They will be treated as separate methods, specific to each class.

"""