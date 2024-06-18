
# problem 1
import math

class test:
    a = 8

    def __init__(self, a=5):
        self.a = a
        print(self.a)


foo = test(2)

# problem 2

print(-1 + math.pi)


# problem 3
"""
The symmetric_difference() method returns a new set that contains all the elements that are in either s1 or s2, but not in both. hence there will
be 8 elements in resulting set {0, 1, 3, 9, 10, 40, 50, -10}
"""
s1 = {50, 40, 30, 20, 10}
s2 = {30, 20, 0, -10, 9, 1, 3}
s3 = s1.symmetric_difference(s2)
print(s3)


# problem 4
n = 0
while n < 10:
    if n % 2 == 0:
        n += 2
        continue
    else:
        break
    print(n)
    n += 1
print('Finished') # it will just print Finished
"""
Explanation:

Initialization: n is initialized to 0.
While Loop Condition: The loop continues as long as n is less than 10.
First Iteration (n = 0):
The condition n % 2 == 0 is True (0 is even).
n is incremented by 2, becoming 2.
The continue statement is encountered, which immediately starts the next loop iteration, skipping the print(n) statement.
Second Iteration (n = 2):
The condition n % 2 == 0 is True (2 is even).
n is incremented by 2, becoming 4.
The continue statement is encountered again, starting the next loop iteration.
Third Iteration (n = 4):
The condition n % 2 == 0 is True (4 is even).
n is incremented by 2, becoming 6.
The continue statement is encountered again.
Fourth Iteration (n = 6):
The condition n % 2 == 0 is False (6 is even).
The else block is executed.
The break statement is encountered, immediately terminating the loop.
Outside the Loop:
Since the loop was terminated by the break statement, the print(n) statement inside the loop is never executed.
The print('Finished') statement after the loop is executed, producing the output "Finished".
"""

