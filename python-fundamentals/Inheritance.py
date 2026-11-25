# class Person:
#     def __init__(self,name):
#         self.name = name
#         print("Person constructor called")
#
#     def show(self):
#         print("Name:",self.name)
#
# class Student(Person):
#     def __init__(self,name,rollno):
#         super().__init__(name) # ye ab parent waly name ko call kry ga
#         self.rollno = rollno
#         print("Student constructor called")
#
#
#     def study(self):
#         print(self.name, "is studying")
#
# s = Student("Ali",101)
# print(s.name)
# print(s.rollno)

# what happend if child class did not have init
# class Person:
#     def __init__(self,name):
#         self.name = name
#
# class Student(Person):
#     pass
#
# s = Student("Ali")
# print(s.name)

### Method Overriding in Python
# class Animal:
#     def sound(self):
#         print("Some animals make sound")
#
# class Dog(Animal):
#     def sound(self):
#         super().sound()
#         print("Dogs make sound: Bohhh")
#
# class Cat(Animal):
#     def sound(self):
#         print("Cats make sound: Meow")
#
# # Now we will create two objects of dog and cat and see which sound called
# d = Dog()
# c = Cat()
#
# d.sound()
# c.sound()

### Now we will use super() in construcotr
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#
# class Developer(Employee):
#     def __init__(self,name,salary,language):
#         super().__init__(name,salary) # it forces to call name and salary of parent class
#         self.language = language
#
# dev = Developer("ALi",23000,"Java")
# print(dev.name)
# print(dev.salary)
# print(dev.language)

### Multilevel Inheritance
# class Animal:
#     def eat(self):
#         print("All animals eat!")
#
# class Mammal(Animal):
#     def walk(self):
#         print("Mammal walk!")
#
# class Dog(Mammal):
#     def bark(self):
#         print("Dog bark!")
#
# dog = Dog()
# dog.eat()
# dog.walk()
# dog.bark()

### Hierachical Inheritence
# (ak hi class sy bht sari child classes bnai jati hy )
#
# class Animal:
#     def __init__(self):
#         print("Eating")
#
# class Dog(Animal):
#     def __init__(self):
#         print("Barking")
#
# class Cat(Animal):
#     def __init__(self):
#         print("Meowing")


### Multiple Inheritance
# is ma ak child class more than one parent class ko extend krti hy
# class Father:
#     def skill1(self):
#         print("Coding")
#
# class Mother:
#     def skill2(self):
#         print("Coocking")
#
# class Child(Father, Mother):
#     def skill3(self):
#         print("Playing chess")
#
# child = Child()
# child.skill1()
# child.skill2()
# child.skill3()


### Hybrid Inheritance with MRO Concept
# class A:
#     def show(self):
#         print("A")
#
# class B(A):
#     def show(self):
#         print("B")
#
# class C(A):
#     def show(self):
#         print("C")
#
# class D(B,C):
#     pass
#
# d = D()
# d.show()
#
# # check mro
# print(D.mro())
# print(D.__mro__)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, roll_no, marks):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.marks = marks

    def get_grade(self):
        if self.marks >= 80:
            return "A"
        elif 60 <= self.marks < 80:
            return "B"
        elif self.marks < 60:
            return "C"
        else:
            return "Invalid marks"

    def display(self):
        super().display()
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)


class SportsStudent(Student):
    def __init__(self, name, age, roll_no, marks, sport):
        super().__init__(name, age, roll_no, marks)
        self.sport = sport

    def display(self):
        super().display()
        print("Sport:", self.sport)


def show_details(person):
    person.display()

    if isinstance(person, Student):
        print("Grade:", person.get_grade())


p = Person("Ali", 20)
s = Student("Ahmed", 21, 101, 85)
ss = SportsStudent("Sara", 24, 45, 90, "Cricket")

show_details(p)
print("----------")
show_details(s)
print("----------")
show_details(ss)