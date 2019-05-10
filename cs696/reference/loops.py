
## Loops: FOR, WHILE

# # use the range(10) function, instead of: i=0, i<10, i++
# for i in range(10):
#     print(i)


# # range(start, stop, step)
# for i in range(20, 30, 2):
#     print(i)


# # while loops
i = 0
while i < 10:
    #print(i)
    i += 1  # not i++


# skip to the next iteration of a loop with CONTINUE
for i in range(100):
    if i%2 == 0:
        continue
    print(i)


# exit a loop entierly with BREAK
# for i in range(5):
#     for j in range(1000000000000000000000000000000000000):
#         if j > 3:
#             break
#         print(i,j)


# # looping over arrays is easy
# x = [1, 2, 3, 4, 5]
# for i in x:
#     print(i)


# # use enumerate to loop over an iterable and count each loop
x = ['one', 'two', 'three', 'four','four']
for i, word in enumerate(x):
     print(i, word)


# # use zip() to loop over two iterables, it will always stop at the shorter of the two
#x = [2, 3, 4, 5, 6, 7, 8, 9]
#y = ['even', 'odd']
#
# for a, b in zip(x, y):
#     print(a, b)

def inf_args(*args):
    """
$   This generator should accept unlimited arguments, and yield them in order. Once all arguments have been yielded,
     this generator should start over, yielding all arguments again, and repeat this pattern INFINITE times
    EX: (1, 4, 'yes', []) -> 1, 4, 'yes', [], 1, 4, 'yes', [], ...
    """
    return_data = []
    while True:
        for letter in args:
            return_data.append(letter)
        yield return_data
x = inf_args(1, 4, 'yes', [])
for i in x:
    print(i)









