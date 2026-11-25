# Positional Parameters
from unittest import result

from pip._internal.req import req_uninstall


# def add_number(a,b):
#     return a + b
# result = add_number(5,6)
# print(result)

# Named Paramters
# def add_number(a,b):
#     return a + b
# result = add_number(b=12,a=13)
# print(result)

# Hybrid Parameter
# def student_info(name,age=12,city="Bwp"):
#     return name,age,city
# result = student_info("Sajid",age=22,city="Mul")
# print(result)

# default Parameters
# without greeting
def greeting(name,greeting="hello"):
      return name,greeting
result = greeting("Sajid")
print(result)

# with greeting
result2 = greeting("Sajid","Hello")
print(result2)



