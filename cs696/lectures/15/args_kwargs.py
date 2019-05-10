"""
Args and Kwargs (and Lambda)

Docs:
https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists
https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments

This section will focus on the different methods for inputs to definitions
"""
import sys

### Default arguments for definitions
def three_arguments(a=0, b=1, c=2):
   print("A is: {}, B is {}, C is {}".format(a, b, c))
#return
#
three_arguments()              # A is: 0, B is 1, C is 2
three_arguments(9)             # A is: 9, B is 1, C is 2
three_arguments('yes', 'no')   # A is: yes, B is no, C is 2





### What is *Args?

# ## The print definition takes in... unlimited arguments?
# print('yes')
# print('yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no')
# # what if I want to write my own definition that takes in any number of arguments?... *args!







# def what_are_args(*args):
#     print(*args)  # try printing 'args' without the *, what changed?
#     return None
#
# what_are_args('hello', 2, [1], {'key': 'value'})
# print('hello', 2, [1], {'key': 'value'})
# # both of these lines print the same thing,
# # this is because *args unpacks all of the arguments into comma separated arguments for the print statement
# # *args passes all of the arguments to the print statement exactly as they were supplied to 'what_are_args()'








# # *args is NOT the same as using a list for inputs
# def why_not_lists(my_list):
#     print(my_list)
#     return None
#
#
# why_not_lists(['hello', 2, [1], {'key': 'value'}])  # prints  ['hello', 2, [1], {'key': 'value'}]
# print('hello', 2, [1], {'key': 'value'})            # prints  hello 2 [1] {'key': 'value'}
# # we could modify the definition so that the two outputs look the same,
# # but functionally, it will still only be supplying 1 value to the print statement, and not 4 separate values
# # this new functionality will allow us to do cool new things that we will see shortly





# ## *arg vs arg: what does the * do?
# # lets just print both
# def my_def(*args):
#     print(*args)    # hello 2 [1] {'key': 'value'}
#     print(args)     # ('hello', 2, [1], {'key': 'value'})
#
# my_def('hello', 2, [1], {'key': 'value'})
# # args is a single object, *args unpacks each of those objects into individual objects for a definition





# def my_def(*args):
#     # print(type(*args))    # error, cannot unpack values into type: type only takes 1 or three arguments
#     print(type(args))       # <class 'tuple'>
#
# my_def('hello', 2, [1], {'key': 'value'})
# # args (without the *) is a tuple of the inputs






# def my_def(*my_args):        # naming the variable 'args' is just a convention, it can be named anything, the * is whats important
#     print(my_args[0:2])      # the tuple args can be subscripted (it can do everything a tuple can)
#
# my_def('hello', 2, [1], {'key': 'value'})











### **KWArgs


# ## Introduction to Key Word Arguments - key/value pair inputs
# # We know print() can take in *args, but it can also take in **kwargs too
# print('Roy', 'Pam')
# # this prints 'Roy' and 'Pam' separated by ' ', which is the default argument





# print('Roy', 'Pam', sep='Jim')
# # this prints 'Roy' and 'Pam' separated by 'Jim'
# # 'sep' is the key word argument






# print('Roy', 'Pam', sep='Jim', end='\tMichael')
# # the default value for end is '\n'
# # key word arguments are used frequently in python modules (less so when scripting)





# ## Accepting  **Kwargs
# def what_are_kwargs(**kwargs):
#     print(kwargs)           # {'my_kw': True, 'your_kw': 10, 'something_lines': False}
#     print(type(kwargs))     # <class 'dict'>
#     return
#
# what_are_kwargs(my_kw=True, your_kw=10, something_lines=False)
# # kwargs (without the stars) really is a dictionary






# ## Use .get() with kwargs! Avoid kwargs[my_key]
# # BAD example
# def my_kwargs(**kwargs):
#     my_name = kwargs['name']
#     my_food = kwargs['food']
#     print('Name is {}, Food is {}'.format(my_name, my_food))
#
# my_kwargs(name='Stanley', food='Pretzel')  # no issues!   but what if we dont use food
# my_kwargs(name='Stanley')                  # KeyError: 'food'
# # this is why we use kwargs.get(food, default_value_here) instead of kwargs[food]






# # GOOD example
# def my_kwargs(**kwargs):
#     my_name = kwargs.get('name', None)
#     my_food = kwargs.get('food', 'Meatballs')
#     print('Name is {}, Food is {}'.format(my_name, my_food))
#
# my_kwargs(name='Stanley', food='Pretzel')  # no issues
# my_kwargs(name='Stanley')                  # Food becomes default value of 'Meatballs'






# # BEST example
# def my_kwargs(**kwargs):
#     my_name = kwargs.get('name', None)
#     if my_name is None:
#         raise Exception('Name is required, no key word argument "name" found')
#
#     my_food = kwargs.get('food', 'Meatballs')
#     print('Name is {}, Food is {}'.format(my_name, my_food))
#
# my_kwargs(name='Stanley', food='Pretzel')  # no issues
# my_kwargs()                                # Exception: Name is required, no key word argument "name" found





# ## Kwargs can be passed through and unpacked if ** is included
# def do_something(my_str, **kwargs):
#     print(my_str, my_str, **kwargs)  # remember ** will unpack the dictionary into individual key word arguments
#     return
#
# do_something('test1')
# do_something('test2', end='<><>', sep='()()')




# # Here is the same example, but kwargs is passed to the print statement, instead of **kwargs
# def do_something(my_str, **kwargs):
#     print(my_str, my_str, kwargs)  # kwargs is a regular dictionary
#     return
#
# do_something('test1')
# do_something('test2', end='<><>', sep='()()')




# # But be careful! some defs may raise Exceptions if extra KWARGS are provided that it doesn't know how to handle
# def do_something(my_str, **kwargs):
#     print(my_str, my_str, **kwargs)
#     return
#
# do_something('test1', end='<><>', food='Pretzels')  # TypeError: 'food' is an invalid keyword argument for print()




# # Work around? remember ** will unpack ANY dictionary, so make a new dictionary from kwargs that is only for print()
# def do_something(my_str, **kwargs):
#     kwargs_for_print = {k:v for k,v in kwargs.items() if k == 'sep' or k == 'end'}
#     print(my_str, my_str, **kwargs_for_print)
#     return
#
# do_something('test1', end='<><>', sep='()()', food='Pretzels')  # No errors, key 'food' is never passed to print()





### Putting it all together! normal arguments + default arguments + *args + **kwargs


# ## Order matters!
# def do_good_thing(x, y, z=10, *args, **kwargs):
#     return
#
# def do_bad_thing(x=10, y, z):  # Error, default param follows non default param
#     return
#
# do_good_thing(1, 2)  # x is 1, y is 2, z is 10
# do_bad_thing(1, 2)   # x is 1, y is 2, z is undefined (causing an error)






# def do_another_bad_thing(*args, x, y, z=10):
#     return
#
# do_another_bad_thing(1, 2, 3, 4, 5, 6, 7, 8, 9)  # args is 1-9, x is undefined, y is undefined, z is 10
# # *args can never come before a variable without a default value,
# # *args will take in unlimited inputs and leave nothing for x and y,
# # (z will be fine, but it will always be 10, so it may as well not be an argument)







## Advanced use of * and **
# if you're comfortable with * or ** you can use them to unpack values wherever you want

# def three_arguments(a=0, b=1, c=2):
#     print("A is: {}, B is {}, C is {}".format(a, b, c))
#     return
#
# my_list = [10, 100, 1000]
# three_arguments(*my_list)   # each element of my_list is unpacked into each input for three_arguments
# three_arguments(my_list)    # 'a' becomes all of my_list while 'b' and 'c' become their defaults
#
# my_list = [10, 100]
# three_arguments(*my_list)   # Only two elements are unpacked, 'c' becomes default
#
# my_list = [10, 100, 1000, 10000]
# three_arguments(*my_list)   # TypeError: three_arguments() takes from 0 to 3 positional arguments but 4 were given





# # Using * or ** isn't reserved just for definitions and args, it will try to unpack anything
# my_list = [1, 1, 1]
# new_list1 = [0, 0, 0, my_list]    # list becomes index 3, total length 4, [0, 0, 0, [1, 1, 1]]
# new_list2 = [0, 0, 0, *my_list]   # each value unpacked, total length 6, [0, 0, 0, 1, 1, 1]
# print(new_list1, new_list2, sep='\n')
# If you're not comfortable with *, you can always just add lists [0, 0] + [1, 1, 1] -> [0, 0, 1, 1, 1]



# # # The same thing can be done with dictionaries and **
# my_dict = {'a': 1, 'b': 2, 'c': 3}
# new_dict1 = {'x': 9, 'y': 9, 'c': 9, **my_dict}  # 'c': 9 will be overwritten when my_dict is unpacked
# print(new_dict1)
# # This is the simplest way to merge(add) dictionaries in python
# # combined_dict = {**my_dict1, **my_dict2}
# # Overlap between the two dictionaries will be resolved by holding the most recent key/value added (from dict 2)
# print({'a': 3, 'a': 4})  # the last value will overwrite the first


