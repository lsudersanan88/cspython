def print_even(my_list):
    """
    Given a list of integers, print only the even numbers
    """
    for i in my_list:
        if i%2 == 0:
            print(i)
    return

# Test case
print_even([1, 2, 3, 4, 6, 9,10])



def square(my_object):
    """
    Use assert or try/except to check if the input can be squared
    """
    try:
        my_object = int(my_object)
        print(my_object**2)
    except:
        print("Cannot square since not a number")
    return

# # Test cases
square(3)
square('hello')


def madlib(adjective_1, adjective_2, adjective_3, noun_1):
    """
    This definition should take in 4 strings, format them into the string below, and print the final string.
    The (adjective_1) man entered the (adjective_2) building to visit a very (adjective_3) man. "Sit down, Mr. Smith, can I interest you in any good (noun_1)?
    """
    final_string = "The " + adjective_1 + " man entered the " + adjective_2 + " building to visit a very " + adjective_3 + " man. \"Sit down, Mr. Smith, can I interest you in any good " + noun_1 + "?"
    return final_string

# # Test case
print(madlib('tall', 'nice', 'tall', 'cat food'))  # should print:  The tall man entered the nice building to visit a very tall man. "Sit down, Mr. Smith, can I interest you in any good cat food?




def stop_at_x(my_list, x):
    """
    This definition should sequentially print every item in my_list until the item x is reached
    """
    for indec in my_list:
        if indec == x:
            break
        print(indec)
    return indec

# # Test cases
stop_at_x([1, 2, 3, 9, 1, 2, 3], 9)  # should print 1, and then 2, then 3, then stop before 9 is printed

# use the range(10) function, instead of: i=0, i<10, i++
for i in range(10):
    print(i)

# range(start, stop, step)
for i in range(20, 30, 2):
    print(i)



# # while loops
# i = 0
# while i < 10:
#     print(i)
#     i = i + 1  # not i++
#



# skip to the next iteration of a loop with CONTINUE
for i in range(100):
    if i%2 == 0:
        continue
    print(i)


#
# exit a loop entierly with BREAK
for i in range(5):
    for j in range(1000000000000000000000000000000000000):
        if j > 3:
            break
        print(i,j)


# looping over arrays is easy
x = [1, 2, 3, 4, 5]
length = len(x)
print(length)
for i in range(length):
    print(i)




# use enumerate to loop over an iterable and count each loop
x = ['one', 'two', 'three', 'four']
for i, word in enumerate(x):
    print(i, word)

print(x[:])
print(x[1:-1])
print(x[1:-2])

# use zip() to loop over two iterables, it will always stop at the shorter of the two
x = [2, 3, 4, 5, 6, 7, 8, 9]
print(x[1:4])
print(x[3:5])
print(x[3:])
print(x[:3])
y = ['even', 'odd', 'even']

for a, b in zip(x, y):
    print(a, b)

# Definitions: we will discuss generators, *args, and **kwargs after exam 2
def dbl(x):
    return x*2

print(dbl(30))


b = [10.0, 'girls & boys', (2+0j), 3.14159, 21, 1000, 1877383, 'love', 'hate']
print(b[1:-1])
# to be done yet
# ASSERT is used mostly for testing
# x = 0
# assert x == 1, 'x is not 1'
#

# # this is similar to
# if x != 1:
#     raise AssertionError('x is not 1')

# try/except work similar to if/else statements
x = 'yes'
try:
    x = int(x)
except:
    print('cannot convert to int')
    exit(1)