
### Lab0

```text
Assignment:
Write a program that does the following in order:
1.Asks the user to enter a number “x”
2.Asks the user to enter a number “y”
3.Prints out number “x”, raised to the power “y”.
4.Prints out the log (base 2) of “x”.
```

```python
import math

x = int(input("Enter a numnber x:"))
y = int(input("Enter a numnber y:"))

# prints x raised to power y
print(pow(x,y))

# print log (base 2) of “x”.
print(math.log2(x))
```

output:
```text
Enter a numnber x:2
Enter a numnber y:3
8
1.0
```