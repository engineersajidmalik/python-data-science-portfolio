from Destructuring import age


class Student:

    def __init__(self,age):
        self.__age = age # we make the age private

    @property
    def age(self):
        return self.__age # we safely return the private variable

    @age.setter
    def age(self):
        if age > 0:
            print("Vaild age")
        else:
            print("Invalid")

s1 = Student(23)
s1.age = 29
print(s1.age)
