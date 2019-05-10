"""
Welcome Back! I hope you had a wonderful Spring Break!

Let's go over generators! (finally!)

"""


### Basic Example - random number generator

# # this is the random number generation
from random import randint
# x = randint(1,100)
# print(x)



# in this example, both definitions can give 'n' random integers between 1 and 100
def list_randints(n):
    my_list = []
    for _ in range(n):  # use an underscore if you never intend to use that variable
        my_list.append(randint(1,100))
    return my_list


# this is the same example, using a generator function - notice there is not list to store things in, and no return
def generator_randints(n):
    for _ in range(n):
        yield randint(1,100)



# # calling the list example
# x = list_randints(10)
# for i in x:
#     print('Random int from list is is: {}'.format(i))
#
# # calling the generator example
# x = generator_randints(10)
# for i in x:
#     print('Random int from gen is is: {}'.format(i))



# ## What can we conclude from this example?
# Both lists and generators can be looped over with the same syntax
#   - this makes changing a list to a generator an easy solution to lowering peak memory usage
# Generator syntax has the potential to be more succinct



# ### Examining the memory footprint of generators
# import sys
# # here is how to examine the size of an object in memory
# x = [i for i in range(100)]
# print(sys.getsizeof(x))


# # now lets examine the sizes of the two
# size = 1000000
#
# my_list = list_randints(size)
# my_gen = generator_randints(size)
# print("List Size: {}\nGen Size: {}".format(sys.getsizeof(my_list), sys.getsizeof(my_gen)))



### What about time?

# here is how to examine the time of something (This will show up again when we discuss decorators!)
from time import time, process_time, sleep  # if you only 'import time', you have to call time.time(), time.sleep()
# t0 = time()
# sleep(5)
# t1 = time()
# print(t1 - t0)
#
# # same demo as above, except with process_time() - notice how it ignores sleep()
# t0 = process_time()
# sleep(5)
# # z = [x for x in range(1000000)]
# t1 = process_time()
# print(t1 - t0)


# ## Comparing time to initialize list and generator
# t0 = process_time()
# my_list = list_randints(1000000)
# t1 = process_time()
# list_init = t1 - t0
# print("Seconds to init List: {}".format(t1 - t0))
#
# t0 = process_time()
# my_gen = generator_randints(1000000)
# t1 = process_time()
# gen_init = t1 - t0
# print("Seconds to init Generator: {}".format(t1 - t0))


# ## Comparing time to loop over each element
# t0 = process_time()
# [i for i in my_list]
# t1 = process_time()
# list_loop = t1 - t0
# print("Seconds to cycle List: {}".format(t1 - t0))
#
# t0 = process_time()
# [i for i in my_gen]  # this is the same as list(my_gen)
# t1 = process_time()
# gen_loop = t1 - t0
# print("Seconds to cycle Generator: {}".format(t1 - t0))
#
# print("Total List Time: {}\nTotal Generator Time: {}".format(list_init + list_loop, gen_init + gen_loop))

## What can we conclude so far?
# Generators offer significant memory advantages compared to lists (even more when compared with sets)
# Generators are faster to initialize compared to a list containing the same data
# Generators have comparably equal times to lists once the generator is cycled through


### Caveats of Generators - Why its not ALWAYS a good idea to use generators over lists

# ## You cannot slice or index a generator
# def list_randints(n):
#     my_list = []
#     for _ in range(n):  # use an underscore if you never intend to use that variable
#         my_list.append(randint(1,100))
#     return my_list
#
# def generator_randints(n):
#     for _ in range(n):
#         yield randint(1,100)
#
# my_list = list_randints(1000)
# my_gen = generator_randints(1000)
#
# print(my_list[50:100])
# print(my_gen[50:100])  # TypeError: 'generator' object is not subscriptable


# ## Generators expire once cycled through - lists may take longer to build, but they can be looped over multiple times
# my_list = list_randints(5)
# my_gen = generator_randints(5)
#
# for i in my_list:
#     print(i)
# for i in my_list:
#     print(i)
# print('-----')
# for i in my_gen:
#     print(i)
# for i in my_gen:  # this one prints nothing, my_gen is expired, we could make a new one with generator_randints(5)
#     print(i)


## something



### More Use Cases for Generators

# ## Generator comprehension - its that easy!
# my_list = [randint(0,100) for _ in range(100)]
# my_gen  = (randint(0,100) for _ in range(100))


## Yield Example

# # The yield statement freezes the definition and returns a single value
# def fixed_yield():
#     yield 'yes'
#     yield 'no'
#     yield 'no'
#     yield 10
#     yield [{}, set(), []]
#
# for i in fixed_yield():
#     print(i)


# # A slightly more complicated example
# def numbered_filenames(my_string, n):
#     for i in range(n):
#         yield str(i) + my_string
#
# for i in numbered_filenames('something.txt', 10):
#     print(i)


### Infinite Generators - can't do this with a list

# ## infinite integers
# def infinite_plus_one():
#     i = 0
#     while True:
#         yield i
#         i += 1
#
# for i in infinite_plus_one():  # Be prepared to force stop this script, it will run forever*
#     print(i)

# ## infinite repeated strings
# def inf_strings():
#     my_strs = ['yes', 'no', 'maybe']
#     i = 0
#     while True:
#         yield my_strs[i%3]
#         i += 1
#
# for s in inf_strings():
#     print(s)
#  # But this definition is not truley infinite, eventually 'i' will become too large


### Built-in 'Generators"
# The range() built-in is not a generator. But it shares some properties
# See this for an educational discussion of range(): https://stackoverflow.com/questions/30081275/why-is-1000000000000000-in-range1000000000000001-so-fast-in-python-3?rq=1
##
# ##
# import sys
# x = range(10)
# y = range(10000000000000000)
# print(sys.getsizeof(x), sys.getsizeof(y))  # same size in memory, equal initialization time

# # at the class level, range can get around some of the shortcomings of generators, such as resetting the generator between loops
# for i in y:
#     if i == 10:
#         break
#
# for i in y:
#     print(i) # if y was a normal generator, this would print 11, but it resets to 0
#     break

# you can also subscript the range function
print(range(0, 1000000000, 3)[2000000]) #  and the implementation is fast!
print(range(0, 1000000000, 3)[2:20]) #  and slicing returns a new range object, not a raw generator
print(len(range(0,100000000, 3)))  # and the class even supports len!


## open() is generator we have been using all semester, that yields one line at a time while reading
with open('example.fasta') as infile:
    print(infile.readline())  # first line
    print(infile.readlines())  # the remainder of the file
    print(infile.readlines())  # empty list

## Conclusion
# Generators are awesome, but have some shortcomings. These shortcomings can be worked around at the class level

