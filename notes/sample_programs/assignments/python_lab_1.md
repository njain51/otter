
### lab1

#### Part A: House Hunting
```text
Write a program to calculate how many months it will take you to save up enough money for a down payment. You will want your main variables to be floats, so you should cast user inputs to floats. 1
Your program should ask the user to enter the following variables: 1.The starting annual salary (annual_salary)2.The portion of salary to be saved (portion_saved)3.The cost of your dream home (total_cost)
```

```python

"""
Assignment:
notes/sample_programs/assignments/python_lab_1.pdf

"""

# Get data from user (hardcoded for testing)
#annual_salary= float(input("The starting annual salary: "))
annual_salary=120000
#portion_saved_percent= float(input("The portion of salary to be saved: "))
portion_saved_percent=.10
#total_cost= float("input The cost of your dream home: ")
total_cost=1000000

# define down payment and investment rate of return
portion_down_payment= 0.25*total_cost
investment_return_rate= 0.04

# calculate monthly salary
monthly_salary=annual_salary/12

# calculate number of months taken to reach portion of down payment as it will allow user to own home

current_savings = float(0)
portion_saved=monthly_salary*portion_saved_percent

num_months=int(0)
while(current_savings<portion_down_payment):

    current_savings = current_savings + (portion_saved + current_savings*(investment_return_rate/12))
    num_months+=1
print(num_months)

```

#### Part B: Saving, with a raise
```text
In ps1b.py , copy your solution to Part A (as we are going to reuse much of that machinery). Modify your program to include the following 1.Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage)2.After the 6 th month, increase your salary by that percentage. Do the same after the 12th thmonth, the 18 month, and so on.
```

```python

"""
Assignment:
notes/sample_programs/assignments/python_lab_1.pdf

"""

# Get data from user ( hardcoded for testing)
#annual_salary= float(input("The starting annual salary: "))
annual_salary=120000
#portion_saved_percent= float(input("The portion of salary to be saved: "))
portion_saved_percent=.05
#total_cost= float("input The cost of your dream home: ")
total_cost=500000
#=float("input a semi-annual salary raise: ")
semi_annual_raise=.03
# define down payment and investment rate of return
portion_down_payment= 0.25*total_cost
investment_return_rate= 0.04

# calculate monthly salary
monthly_salary=annual_salary/12

# calculate number of months taken to reach portion of down payment as it will allow user to own home

current_savings = float(0)


num_months=int(0)
while(current_savings<portion_down_payment):
    portion_saved=monthly_salary*portion_saved_percent
    current_savings = current_savings + (portion_saved + current_savings*(investment_return_rate/12))
    num_months+=1

    if(num_months % 6 == 0):
        monthly_salary = monthly_salary + monthly_salary*semi_annual_raise


print("Number of months:", num_months)
```

#### Part C: Finding the right amount to save away

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: ernesto
"""

starting_salary = int(input("Enter the starting salary: "))
semi_annual_rise = 0.07
annual_return = 0.04
total_cost = 1000000
portion_down_payment = total_cost * 0.25
months = 36

min_rate = 0        # 0%
max_rate = 10000    # 100%

portion_saved = int((max_rate + min_rate) / 2)
steps = 0
found = False

while abs(min_rate - max_rate) > 1:
    steps += 1
    annual_salary = starting_salary
    monthly_saved = (annual_salary / 12.0) * (portion_saved / 10000)
    current_savings = 0.0

    for i in range(1, months + 1):
        monthly_return = current_savings * (annual_return / 12)
        current_savings += monthly_return + monthly_saved

        if abs(current_savings - portion_down_payment) < 100:
            min_rate = max_rate
            found = True
            break
        elif current_savings > portion_down_payment + 100:
            break
        
        if i % 6 == 0:
            annual_salary += annual_salary * semi_annual_rise
            monthly_saved = (annual_salary / 12.0) * (portion_saved / 10000)

    if current_savings < portion_down_payment - 100:
        min_rate = portion_saved
    elif current_savings > portion_down_payment + 100:
        max_rate = portion_saved
    
    portion_saved = int((max_rate + min_rate) / 2)
    
if found:
    print("Best savings rate:", portion_saved / 10000)
    print("Steps in bisection search", steps)
else:
    print("Is is not possible to pay the down payment in three years")
```