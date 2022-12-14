"""
This module is a demo code for lecture 5

At this lecture we cover
    - classes
    - OOP principles

Materials
    - see lecture_6.py

"""


#
# 1. so far you have been working with objects with are type of some class
# a = 1
# print(type(a))
# print(dir(a))
# a < 1
# a.__lt__(1)
#
#
# 2. create your first class (attributes and methods)
# class Dog:  # defining a Dog class
#
#     def bark(self):  # defining a bark method
#         print("bark!")
# #
# #
# a_dog = Dog()  # instantiating an Dog class object
# print(type(a_dog))
# a_dog.bark()  # calling .bark() method for the instance
#
#
# print(type(a_dog))  # remember __main__ module, __name__ variable
# print(a_dog)
#
#
# # 3. initialize with __init__ SPECIAL method
# # this method is automatically called once the class is created

# class Dog:
#     """
# Here is the docstring of your class
# where you can and most preferably should add doc of the class
# multiline is supported
# 	"""
#
#     # here are some class attributes
#     number_of_legs = 4
#     number_of_eyes = 2
#     family = "canidae"
#
#     def __init__(self, name: str, age: int):
#         """
# When creating a new Dog class object it MUST
# have a name name of the dog
#
# 		"""
#         self.name = name  # here we assign a function argument to an instance, identifiers may not match
#         self.age = age  # type hinting
#
#     def bark(self) -> None:
#         print("bark!")
#
#
# a_dog = Dog("Max", 3)
# print(type(a_dog.age))
# print(a_dog.number_of_eyes)
# print(a_dog.name)
# # print(Dog.bark())

#
# # 4. changing attributes
#

# class Dog:
#     number_of_legs = 4
#
#     def __init__(self, given_name, age):
#         self.name = given_name
#         self.age = age
#
#     def change_name(self, new_name):
#         self.name = new_name
#
#     def lose_a_leg(self):
#         if self.number_of_legs > 0:
#             self.number_of_legs -= 1
#
#
# a_dog = Dog("Max", 3)
# print(a_dog.name)
# a_dog.change_name("Stewart")
# print(a_dog.name)
#
# print(f"{a_dog.name} had {a_dog.number_of_legs} legs")
# a_dog.lose_a_leg()
# a_dog.lose_a_leg()
# print(f"Now {a_dog.name} has {a_dog.number_of_legs} legs")

#
# # 5. let's code now
# # class Student - init with name, age, prev_grade
# # class Course - init with name, max_students, students
# # with add_student
#
#
# # 6. inheritance
# class Person:
#     number_of_legs = 2
#     number_of_eyes = 2
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def introduce(self):
#         print(f"Hello! I am {self.name} and I am {self.age} y.o.")
#
#
# class Student(Person):
#
#     def set_university_year(self, university, year):
#         self.university = university
#         self.year = year
# #
#
# class Driver(Person):
#
#     def set_driver_info(self, licence_num, experience, *cars):
#         self.licence_num = licence_num
#         self.experience = experience
#         self.cars = cars
# #
# #
# st = Student(name="Ann", age=20)
# st.set_university_year("YSU", 2)
#
# dr = Driver("Alice", 44)
# dr.set_driver_info(1009986, 23, "toyota", "acura", "land rover")
# print(dr.cars)
#
#
# # 7. super.__init__(), superclass or upper-level class or parent class

# class Person:
#     number_of_legs = 2
#     number_of_eyes = 2
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def introduce(self):
#         print(f"Hello! I am {self.name} and I am {self.age} y.o.")
#
#
# class Student(Person):
#
#     def __init__(self, name, age, university, year):
#         super().__init__(name, age)  # difference from self.age = age; self.name = name
#         self.university = university
#         self.year = year
#
#
# st = Student("Al", 24, "MIT", 4)
# st.introduce()
# print(f"I have {st.number_of_legs} legs")
# print(f"Year of studies: {st.year}")


# # decorators (functional programming)
#
# 8. class methods
# self keyword is a reference to instance attributes
# # cls keyword is a reference to class attributes
#
# class Student:
#     number_of_students = 0
#
#     def __init__(self, name, university):
#         self.name = name
#         self.university = university
#         Student.add_student()
#
#     @classmethod
#     def add_student(cls):
#         cls.number_of_students += 1

#
# print(f"Current number of students: {Student.number_of_students}")
# print(f"Current number of students: {Student.number_of_students}")
# st1 = Student("Al", "TUM")
# print(f"Current number of students: {Student.number_of_students}")
# print(f"Current number of students: {st1.number_of_students}")
# st2 = Student("Berg", "EPFL")
# Student("a", 5)
# print(f"Current number of students: {Student.number_of_students}")
# print(f"Current number of students: {st1.number_of_students}")
# print(f"Current number of students: {st2.number_of_students}")

#
# # 9.static methods
# # static methods act like functions
# # they don't access anything, they don't mutate anything
# # # let's call this module from another script
# #
# class MyFunctions:
#
#     @staticmethod
#     def upper(x):
#         if isinstance(x, str):
#             return x.upper()
#
#     @staticmethod
#     def capitalize(x):
#         if isinstance(x, str):
#             return x.capitalize()

###################################################

class Person:

    def __init__(self, name):
        self.name = name


armen = Person(name='Armen')
print(armen.name)
