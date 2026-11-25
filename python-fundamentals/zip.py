# Part C: zip()

"""
Q16. Create two lists: student names and marks. Use zip() to display each student's name
with mark
"""
from Collections import countries

std_names = ["Ali","Ahmad","Raza"]
std_marks = [90,10,80]
print(list(zip(std_names,std_marks)))

"""
Q17. Create two lists: products and prices. Display only the products whose price is greater 
than 500.
"""
products = ["Sunglasses","Watch","Laptop","AC"]
prices = [100,10000,65000,499]

for product, price in zip(products, prices):
    if price > 500:
        print(product)

"""
Q18. Create two lists: countries and capitals. 
Use zip() to print each country with its capital.
"""
countries = ["Pak","India","Japan","China"]
capitals = ["Isl","Delhi","Tokyo","Beijing"]

print(list(zip(countries,capitals)))

"""
Q19. Create three lists: employee names, departments, and salaries. 
Use zip() to display all employee records.
"""
employee_names = ["Waseem","Usman","Usama","Zeeshan"]
departments = ["SE","CS","IT","AI"]
salaries = [90000.0,100000.0,60000.0,45000.0]

print(list(zip(employee_names,departments,salaries)))

# Also other version of it
for emp,dep,sal in zip(employee_names,departments,salaries):
    print(emp,dep,sal)

"""
Q20. Create two lists: subjects and obtained marks. 
Use zip() to calculate and display the total obtained marks
"""
std_subjects = ["Math","Eng","Comp"]
std_obtained_marks = [90,77,80]
total_obtained_marks = 0

for sub,marks in zip(std_subjects,std_obtained_marks):
    total_obtained_marks += marks
print("Total marks are:", total_obtained_marks)
