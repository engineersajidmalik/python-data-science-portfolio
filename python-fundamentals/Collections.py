"""
Part A: Collections Practice Questions
"""
from itertools import count
from subprocess import check_output

from pip._internal.utils import appdirs

"""
Q1. Create a list of 10 integers. Print all the numbers greater than 50
"""
list = [10,20,30,40,50,60,70,80,90,100]
# We will solve this using Range Syntax is: [start:stop:step]
print("The integer >50 are:",list[5::])
## We can also solve it using for loop
for num in list:
    if num > 50:
        print(num)

"""
Q2. Create a list of five fruits. Add two new fruits, remove one fruit,
 and display the updated list. 
"""

fruits= ["Apple", "Mango", "Orange", "Banana", "Cherry"]
print(fruits)
# Add 2 new fruits
fruits.append("Grapes")
fruits.append("Orange")
# Remove one Fruit
fruits.remove("Apple")
print("After removing 1 fruit the list will be :", fruits)


"""
Q3. Create a tuple containing five student names. Print each name using a for loop. 
"""
"""
The syntax fo for loop is: for item in iterable:
item = ak temp name, iterable = us list ka name jisko loop ma chalana hy 
"""
std_names = ("Ali", "Ahmad", "Raza", "Ramzan", "Shahmeer")
for name in std_names:
    print(name)

"""
Q 4: Create a set of eight numbers. Print only the even numbers. 
"""
numbers = {1,2,3,4,5,6,7,8}
## Set is an unordered so we can not solve it using slicing
# we will solve it using for loop and a modulo operator

for n in numbers:
    if n % 2 == 0:
        print(n)

"""
Q5. Create a dictionary containing five students and their marks. 
Display all student names and marks. 
"""
students = {"Ali":10, "Ahmad":20, "Raza":30, "Rehan":40, "Azan":50}
for name, marks in students.items():
    print(name,":", marks)

"""
Q6. Create a dictionary of five products and their prices. 
Print only the products whose price is greater than 1000.
"""
products = {"iPhone":150000, "Samsung":10000, "Charger":500, "Cable":300, "Screen":1500}
print("The products whose price is > 1000 are:")
for product, price in products.items():
    if price > 1000:
        print(product,":",price)

"""
Q7. Create a list of ten numbers. 
Count how many numbers are even and how many are odd.
"""
TenNumbers = [1,2,3,4,5,6,7,8,9,10]
# For counting we need to initialize count even and odd
count_even = 0
count_odd = 0
for number in TenNumbers:
    if number % 2 == 0:
        count_even += 1

    if number % 2 != 0:
        count_odd += 1

print("Count_Even are:", count_even)
print("Count_Odd are:", count_odd)

"""
Q8. Create a list containing the marks of eight students. 
Find and print the highest and lowest marks.
"""
marks_of_students = [80, 90, 76, 33, 80, 45, 19, 77]
print("Highest marks are:",max(marks_of_students))
print("Lowest marks are:",min(marks_of_students))

"""
Q9. Create a dictionary containing five countries and their capitals. 
Print only the country names.
"""
countries = {"Pakistan":"Islamabad", "India":"Delhi", "China":"Beijing", "Russia":"Moscow", "USA":"Washinton"}
for country in countries.keys():
    print(country)

"""
Q10. Create a list containing positive and negative numbers. Print only the positive 
numbers.
"""
p_and_n_numbers = [1,-1,2,-2,3,-3,4,-4,5,-5]
for num in p_and_n_numbers:
    if num > 0:
        print(num)
