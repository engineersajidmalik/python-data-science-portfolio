import time


# def add_greeting(func):
#
#     def wrapper():
#         print("Hi")
#         func()
#         print("Goodbye")
#     return wrapper
#
# @add_greeting
# def say_name():
#     print("I am Sajid")
#
# say_name()

# Time decorator that will sleep for 5 seconds
# def timer(func):
#
#     def wrapper():
#         start = time.time() # before
#         func() # original
#         end = time.time() # after
#     return wrapper
#
# @timer
# def slow_function():
#     time.sleep(2) # waits for 2 seconds
#     print("Done")
#
# slow_function()

# Create a star boarder
def star_boarder(func):

    def wrapper():
        print("**********")
        func()
        print("**********")
    return wrapper


# apply that decorator to the function below
@star_boarder
def say_hello():
    print("Hello Python learner ")

# call the function
say_hello()

