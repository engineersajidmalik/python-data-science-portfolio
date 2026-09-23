"""
Q11. Create a list of five student names.
Use enumerate() to print the index and student name.
"""
student_names = ["Ali", "Ahmad", "Wasif", "Waseem", "Shahmeer", "Rizwan"]
print(list(enumerate(student_names)))

"""
Q12. Create a list of six programming languages. 
Use enumerate(start=1) to print serial numbers with each language.
"""
programming_languages = ["Python", "C", "C++", "Java", "Ruby","Julia"]
print(list(enumerate(programming_languages, start=1)))

"""
Q13. Create a list of eight numbers. 
Use enumerate() to display the index of every number greater than 50.
"""

numbers = [10,20,100,50,60,70,80,90]
for index,num in enumerate(numbers):
    if num > 50:
        print(index,"=",num)


"""
Q14. Create a list of five cities. Print only the cities stored at even indexes using 
enumerate().
"""
cities = ["Bwp", "Mul", "Fsd", "Lhr", "Isl"]
for index, city in enumerate(cities):
    if index % 2 == 0:
        print(city,"=", index)


"""
Q15. Create a list of six subjects. Display them as Subject 1, Subject 2, etc. using 
enumerate().
"""
subjects = ["Math","Eng","Bio","Phy","Chem","Isl"]
for index, subject in enumerate(subjects, start=1):
    print("Subject", index, "=", subject)
