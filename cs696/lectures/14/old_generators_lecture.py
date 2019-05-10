"""
Lecture 10

    - Generators
    - Yields

"""
"""
Remember this result from exercise_09?

@time_decorator
def list_comp():
    return [x for x in range(1,1000000)]

@time_Decorator
def generator_comp():
    return (x for x in range(1,1000000)

def             time    size
list_comp       0.04    4348736
generator_comp  0       48

So whats the story? Why is the generator instant and only 48 bytes?

"""

from templates.exercise_09 import time_decorator
import math
from memory_profiler import profile  # add the decorator @profile to examine the memory used by a definition

@time_decorator
def list_log():
    numbers = [x for x in range(1,1000000)]
    return [math.log10(x) for x in numbers]

@time_decorator
def gen_log():
    numbers = (x for x in range(1,1000000))
    return (math.log10(x) for x in numbers)  # generators can be inside of generators - no problems here

# list_log()
# gen_log()






# Another function that takes in a function, this one just cycles through each value in our list and generator

@time_decorator
def cycle_all(my_function):
    x = my_function()
    for i in x:
        pass
    return x

# cycle_all(list_log)
# cycle_all(gen_log)










# Custom Generators vs returning a list
def list_log():
    my_list = []
    for i in range(1,1000000):
        my_list.append(math.log10(i))
    return my_list

def gen_log():
    for i in range(1,1000000):
        yield math.log10(i)





for i in list_log():
    pass

for i in gen_log():
    pass


# Infinite Generators!

def doubles_forever():
    i = 1
    while True:
        yield i
        i = i * 2

# x = doubles_forever()
# print(x)  # generator object at 0x00000000
# print(next(x)) # next(x) = 1   ->    print(1)
# x = next(x) # NOOOOOOO NEVER DO THIS!!!!!!!!!!!!!!!!!!
# next(x)   # next is still called, but value is never saved
# print(x)  # still generator object at 0x00000000
#
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))




# What is the first number in the series double_number(), that occurs after 10,000,000?
# 10,000,001 to 13,000,000
# 13,000,001 to 16,000,000
# 16,000,001 to 19,000,000
# 19,000,000 +
# for i in doubles_forever():
#     if i > 10000000:
#         print(i)
#         break


# Reading a massive file:
# x = 0
# with open('my_file.txt', 'r') as infile:
#     for line in infile:
#         x += sum(line)



