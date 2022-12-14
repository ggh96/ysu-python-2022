"""
This module is a demo code for lecture 8

At this lecture we cover
    - iterators, generators
    - open(), with and context managers
    - OOP recap

Materials
    - Dusty Phillips, Python 3 Object-oriented Programming - Chapter 9
    - Michael T. Goodrich, Data Structures and Algorithms in Python - Chapter 1.6, 1.8

    also:
    - https://realpython.com/python-with-statement/
    - https://www.youtube.com/watch?v=Lv1treHIckI&list=PLzMcBGfZo4-kwmIcMDdXSuy_wSqtU-xDP&index=6
    - https://realpython.com/python-with-statement/#managing-resources-in-python
"""

##################################################

#
# __iter__ - Iterable
# __next__ - Iterator
# # # iterators - __iter__(), __next__()
# # iter should return the object itself
# # next should return the next element
# # https://github.com/python/cpython/blob/3.10/Lib/_collections_abc.py
#

a = range(10000000000)
print(a)
print(a.__sizeof__())

# #
# b = [i for i in range(1,10)]
# print(b)

# print(b.__sizeof__())

class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


# rev = Reverse('spam')
# print(rev.__next__())
# print(rev.__next__())
# print(rev.__next__())
# print(rev.__next__())
# print(rev.__next__())
# # for char in rev:
# #     print(char)

#
# generators - yield statement
# def reverse(data):
#     for index in range(len(data) - 1, -1, -1):
#         yield data[index]
#
# a = reverse("spam")
# print(a)
#
# print(next(a))
# print(next(a))
#
# # generator comprehension
# [i**2 for i in [1,2,3]]
# gen = (elem for elem in range(10) if elem % 3 == 0)
# print(gen)
# print(elem for elem in gen)
#
# a = (13,14,15)
# n = ("a","b","c", "a")
# g = ("a","b","b",1 , 2)
#
# z = zip(a,n,g)
# print(z)
# for elem in z:
#     print(elem)

# # range()
# # zip()
#
#
# reverse('abc')
# print(reverse('abc'))
#
# a = reverse('abc')
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# # print(a.__next__()) # will raise StopIteration exception
#
# a = reverse('abc')
# for elem in a:
#     print(elem)
# zip
###################################
# # # context managers
# # __enter__ and __exit__ methods
# # python i/o
#
# print(open.__doc__)
# path = "../data/zen_of_python.txt"
#
# # read entire file
# file = open(path, "r")
# print(file)
# print(file.__dir__())
# text = file.read()
# print(text)
#
# # read line by line
# file = open(path, "r")
# print(file)
# for line in file:
#     print(line, end="")
#
# # open as context manager
# with open(path, "r") as file:
#     for line in file:
#         print(line, end="")
#
# # append with the context manager
# with open(path, "a") as file:
#     for num in range(5):
#         file.write("a line is added\n")

# # write with the context manager
# with open("../data/a_new_random_file.txt", "w") as file:
#     for num in range(5):
#         file.write("a line is added\n")
#