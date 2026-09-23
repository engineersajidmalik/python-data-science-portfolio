"""
Q26. Create two lists: student names and marks.
Use zip() and enumerate() to display the records with serial numbers.
"""
from turtledemo.penrose import start

from zip import departments

std_name = ["Ali","Ahmad","Raza"]
std_marks = [22,45,67]

for serial, (name,marks) in enumerate(zip(std_name,std_marks), start=1):
    print(serial,name,marks)

"""
Q27. Create three lists: employee names, departments, and salaries. 
Use zip() to display only the employees working in the IT department.
"""
emp_name = ["Jawad","Rehan","Naeem"]
departments = ["CS","SS","IT"]
salaries = [2000,4500,6700]

for name,depart,sal in zip(emp_name,departments,salaries):
    if depart == "IT":
        print(name,depart,sal)

"""
.
Q28. Create a list of tuples containing (student_name, marks). 
Use destructuring to print only the students who scored more than 80 marks
"""
student_info = [("Sajid",99),("Shahmeer",80),("uzair",70)]
for name,marks in student_info:
    if marks > 80:
        print(name,marks)

