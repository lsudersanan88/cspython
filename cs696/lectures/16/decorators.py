"""
Lambda
Decorators
Pickle
"""

### Lambda Functions


## Introduction
# some defs accept other defs as arguments, like map(), filter(), and sort()
# map() applys a definition to all elements in an iterable

# my_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# new_list = map(int, my_list)
# print(new_list)  #  map object :(
#
# new_list = list(new_list)
# print(new_list)




# # but we can define our own functions for map as well
# def plus_one(x):
#     return x + 1
#
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# x = map(plus_one, x)  # NOTE that "plus_one" is used as an input, not "plus_one()" or "plus_one(x)"
# print(list(x))
#
# #or with list comp
# x = [plus_one(i) for i in x]





# # filter() is like map, but returns a boolean
# def gt_ten(x):
#     return x > 10   # this returns a boolean
#
# x = [5, 10, 20, 30]
# x = filter(gt_ten, x)
# print(list(x))
#
# #or with list comp
# x = [i for i in x if gt_ten(i)]





# # sort() - this one is much more important than the other two!
# x = [0, 9, 1, 8, 2, 7, 3, 6, 4, 5]
# y = sorted(x)
# print(x)  # sorted() is not 'in-place', you need to save it to a new variable like y
# print(y)





# # sort takes in a definition for custom sorting
# def mod_two(x):
#     return x%2
#
# x = [0, 9, 1, 8, 2, 7, 3, 6, 4, 5]
# y = sorted(x, key=mod_two)
# print(y)
# # in this example, even elements in x are evaluated to priority 0 and odd elements are 1, then they are sorted




# # same example, with a more detailed mod_two()
# def mod_two(x):
#     if x%2 == 0:
#         return 0
#     if x%3 ==0:
#         return 1
#     if x%5 == 0:
#         return 2
#     else:
#         return -1
#
# x = [0, 9, 1, 8, 2, 7, 3, 6, 4, 5]
# y = sorted(x, key=mod_two)
# print(y)
# # in this example, elements divisible by 5 have the highest value,
# # followed by elements divisible by 3
# # followed by elements divisible by 2 (all even numbers)
# # and finally, odd elements that are not divisible by 3 are lowest (all remaining numbers)



# ## SORTING A DICTIONARY BY ITS VALUES
# # I have googled this many times before I memorized it; I believe this is the cleanest solution
# # Also, this is a topic that has been around a long time,
# #  make sure you are not reading stack overflow answers from 2009 suggesting itemgetter
# my_dict = {'a': 1, 'b': 0, 'c': 3, 'd': 100, 'e': -1}
# my_dict['z'] = -100  # adding this to the end of our dictionary
#
# for k,v in my_dict.items():
#     print(k, v)  # dictionary loops and prints in order
#
# x = sorted(my_dict, key=my_dict.get)
# print(x)  # only sorted keys! if we want a new dictionary we have to capture the values too:
#
# x = {k: my_dict[k] for k in sorted(my_dict, key=my_dict.get)}
# print(x)





# ### Lambda functions (one line, anonymous, definitions)
# # https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
# # Lambda functions are a shortcut syntax for creating a definition in one line
# # the syntax is "lambda <input args>: <return value>"
# # for Example:  "lambda my_list: [str(x) for x in my_list]"
#
# def plus_one(x):
#     return x+1
#
# lamb_one = lambda x: x+1
# print(lamb_one(10))
# print(plus_one(10))






# # same example from earlier, but using lambda
# x = [0, 9, 1, 8, 2, 7, 3, 6, 4, 5]
# y = sorted(x, key=lambda x: x%3)
# print(y)






# # lambda can do everything a definition can; What will the output of this code be?
# my_def_3 = lambda **kwargs: [print(k,v) for k,v in kwargs.items()]
# x = my_def_3(me=True, you=False)
# print(x)






### Decorators

## Introducton
# # definitions, can accept definitions as arguments (they're both objects)
# def plus_two(x):
#     return x+2
#
# def print_defname(my_def):
#     print(my_def.__name__)
#     return
#
# print_defname(plus_two)
# print_defname(plus_two())  # ERROR! Remember, adding () calls the definition plus_two, and we're trying to
#                            # use the definition as an argument, not the return statement of plus_two as an argument




# ## Passing through *args and **kwargs
# def plus_two(x):
#     return x+2
#
# def log_defname(my_def, *args, **kwargs):  # now accepts args and kwargs
#     print('LOG: def={}, args={}, kwargs={}'.format(my_def.__name__, args, kwargs))
#     result = my_def(*args, **kwargs)
#     return result
#
# x = log_defname(plus_two, 4)
# print(x)
# # We can now run any def inside of log_defname, log the arguments, AND capture and return the result from the inner def
# # This method preserves functionality for the inner def, and provides a repeatable way to wrap a definition



# ## One last layer of complexity, because decorators must ALWAYS return a definiton, not a result
# def log_decorator(my_def):
#
#     def internal(*args, **kwargs):
#         print('LOG: def={}, args={}, kwargs={}'.format(my_def.__name__, args, kwargs))
#         result = my_def(*args, **kwargs)
#         return result
#
#     return internal
#
# def plus_two(x):
#     return x+2
#
# x = log_decorator(plus_two)  # give log_decorator a single definition
# print(x) # function within a function! not a value, x is a definition!
# # so what do we do with x?
# y = x(4)  # just calling x causes it to print the log AND run and return the value
# print(y)
# # To state again what happend in this example:
#     # 1. x was created by passing the definition plus_two into log_decorator
#     # 2. log_decorator returns a definition called internal
#     # 3. internal is a definition that accepts any args/kwargs, but it was not run at the time it was returned
#     # 4. once x was called with x(4), internal was called with (4)
#     # 5. when internal is called, it prints the def name, args, and kwargs
#     # 6. then internal runs the definition it named with args and kwargs
#     # 7. finally, it captures the result from plus_two, and returns it
#     # note: If you look closely at internal, you will notice it does not accept my_def like log_decorator does,
#     #        it does still have enough scope to see that variable, and when internal is returned, it retains
#     #        knowlege of the variables in its surrounding environment
#     # note: You may also notice that log_decorator does not accept *args or **kwargs, yet internal does.
#     #        This is because the only purpose of log_decorator is to return a wrapped definition,
#     #        it is the INTERNAL definition that will be called with arguments





# ## Decorator syntax
# # exactly the same as before
# def log_decorator(my_def):
#
#     def internal(*args, **kwargs):
#         print('LOG: def={}, args={}, kwargs={}'.format(my_def.__name__, args, kwargs))
#         result = my_def(*args, **kwargs)
#         return result
#
#     return internal
#
# @log_decorator  # apply the decorator to this definition
# def plus_two(x):
#     return x+2
#
# x = plus_two(7) # automatically prints the LOG when called





# ## Without the shortcut @decorator syntax
# # exactly the same as before
# def log_decorator(my_def):
#
#     def internal(*args, **kwargs):
#         print('LOG: def={}, args={}, kwargs={}'.format(my_def.__name__, args, kwargs))
#         result = my_def(*args, **kwargs)
#         return result
#
#     return internal
#
# def plus_three(x):
#     return x+3
#
# x = log_decorator(plus_three)(7)  #this is what is happening when you apply @log_decorator
# x = log_decorator(plus_three(7))  # incorrect, but why? what is x?
# x = log_decorator(plus_three)     # incorrect, but why? what is x?








# # IF ELSE CHAIN EXAMPLE BREAKDOWN
# my_list = [11,10,9,8,7,6,5,4,3,2,1]
# x = [10 if x >= 10 else 9 if x == 9 else 8 if x==8 else 7 if x ==7 else 6 for x in my_list]
# print(x)
#
# newx = []
# for x in my_list:
#     if x >= 10:
#         newx.append(10)
#     else:
#         if x == 9:
#             newx.append(9)
#         else:
#             if x == 8:
#                 newx.append(8)
#             else:
#                 if x == 7:
#                     newx.append(7)
#                 else:
#                     newx.append(6)
# print(newx)
#
# # NOW COMBINE EVERY ELSE STATEMENT FOLLOWED DIRECTLY BY AN IF STATEMENT
# newx = []
# for x in my_list:
#     if x >= 10:
#         newx.append(10)
#     elif x == 9:
#         newx.append(9)
#     elif x == 8:
#         newx.append(8)
#     elif x == 7:
#         newx.append(7)
#     else:
#         newx.append(6)
# print(newx)
# #
# #









### Pickle
# it stores objects/variables in a file - and its this simple

#saving
import pickle
favorite_color = { "lion": "yellow", "kitty": "red" }
pickle.dump(favorite_color, open("save.pickle", "wb"))

# loading
favorite_color = pickle.load(open("save.pickle", "rb"))




















######################################################################
# The following is last years lecture (2018),
# It contains the same information but with timing instead of logging.
######################################################################

"""
REVIEW: Functions are objects, and aren't called until ()
def add_10(n):
    return n + 10

x = add_10
y = add_10(5)

x is a function
y is an integer

x = x(5)
x is now an integer, both y and x equal 15
"""

# lets look at a simple (but pointless) example of what is to come
def zeros():
    return [0]*100

def outer_def(my_function):

    def inner_def():
        result = my_function()
        return result

    return inner_def


x = outer_def(zeros)


"""
Time module in Python:
import time

Syntax                  Action
time.sleep(1)           sleep for (1)
time.time()             returns a float of seconds since epoch (real world time measurement)
time.process_time()     returns a float of seconds equal to process time used since the start of the process (ignores sleep)

"""

# # basic timing example
# import time
#
# t0 = time.time()                    # capture start time as t0
# x = [x**2 for x in range(1000000)]  # run some code
# t1 = time.time()                    # capture end time as t1
# print(t1-t0)                        # print the difference of the two times


# This basic example works fine, but what if we want to time 20 different functions?
# Or maybe we only want to easily choose which functions to time.
# Use decorators!
# Let's merge the timing example, with the zeros() example from earlier.

# def time_decorator(my_def):
#     def internal_wrapper():
#         t0 = time.time()
#         def_result = my_def()
#         t1 = time.time()
#         print("'{}' finished in {} seconds".format(my_def.__name__, t1-t0))
#         return def_result
#     return internal_wrapper # remember, 'internal_wrapper' is not the same as 'internal_wrapper()'
#
# def squares():
#     return [x**2 for x in range(1000000)]
#
# time_decorator(squares)  # note this is "squares" not "squares()"; "squares()" is a list, not a function.

"""
Test Yourself! What is x in each of the following cases?
x = time_decorator(squares)
x = time_decorator(squares())
x = time_decorator(squares())()
"""




# @time_decorator
# def squares():
#     return [x**2 for x in range(1000000)]
#
# squares  # note this is "squares" not "squares()"; "squares()" is a list, not a function.


# What if we want to pass arguments to our decorator?
# Our internal wrapper function needs to accommodate the arguments of many different functions,
# Does this problem sound familiar? (hint: lecture_08)


# def zeros():
#     return [0] * 100
#
#
# def outer_def(my_function):
#
#     def inner_def(*args, **kwargs):
#         result = my_function()
#         return result
#
#     return inner_def
#
#
# x = outer_def(zeros)





