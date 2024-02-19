# def show_name(name):
#     return f"""
#             **************
#             {name}
#             **************
#             """
#
# print(show_name("timi"))
from time import time

from AsendingOrder import count


#
# def decorate(fn):
#     def inner(*args, **kwargs):
#         print("************")
#         print(fn(*args, **kwargs))
#         print("************")
#
#     return inner
#
#
# @decorate
# def show_name(name):
#     return name
#
#
# show_name("timi")

# def time_taken(func):
#     def wrap(*args, **kwargs):
#         t1 = time()
#         result = func(*args, **kwargs)
#         t2 = time()
#         print(f"it took {t2 - t1: 3f}ms to execute")
#
#         return result
#
#     return wrap
#
#
# @time_taken
# def get_list(numbers):
#     result = []
#     for i in range(numbers):
#         result.append(i)
#     return result
#
#
# get_list(10000000000)

# def gun(name, number = 00):
#     return f"{name} & {number}"
# print(gun("izu", 30))

# def gun(name, *number):
#     return f"{name} & {number}"
# print(gun("izu"))
# def get_sentenceIndex():
#     sentence = " the palace is few miles away from the village but going to the palace to see startups in cool and fun"
#     " the palace is few miles away from the village but going to the palace to see startups in cool and fun"
#     for word in sentence:
# print(
#     count(sentence))




