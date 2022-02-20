"""
Assignment:
notes/sample_programs/assignments/python_lab_1.pdf

"""

# Get data from user ( hardcoded for testing)
#annual_salary= float(input("The starting annual salary: "))
annual_salary=150000
#portion_saved_percent= float(input("The portion of salary to be saved: "))
portion_saved_percent=.44
#total_cost= float("input The cost of your dream home: ")
total_cost=1000000
#=float("input a semi-annual salary raise: ")
semi_annual_raise=.07
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