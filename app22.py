#given list
# Emp =['101,raj,sales,1000','102,ram,hr,2000','103,ravi,admin,3000','104,rajesh,finance,4000']
#iterate the given list - step by step
#using membership operator filter sales dept
#split each string (line) into multiple value(list) based on sep(,)
#display Emp name - working dept at the end display sum of emp's cost
...
Emp = ['101,raj,sales,1000', '102,ram,hr,2000', '103,ravi,admin,3000', '104,rajesh,finance,4000']
total_cost = 0
for emp in Emp:
    if 'sales' in emp:
        emp_details = emp.split(',')
        name = emp_details[1]
        dept = emp_details[2]
        cost = int(emp_details[3])
        total_cost += cost
        print(f"Employee Name: {name}, Department: {dept}")

print(f"Total Cost: {total_cost}")

