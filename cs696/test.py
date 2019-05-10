


def printOddNumbersInTheList(args):
    for num in args:
        if (num %2 != 0):
            print(num)

# printOddNumbersInTheList([1,2,3,4,5,6,7,8])


def findEvenNumberInTheList(nums):
    evenNum = []
    for num in nums:
        if num % 2 == 0:
            evenNum.append(num)

    return evenNum

# print(findEvenNumberInTheList([1,2,3,4,5,6,7,8]))

def squareTheNumber(var):
    try:
        float(var)
        return var*2
    except:
        print("Not a number")
# print(squareTheNumber("11"))


def madlib(adjective_1, adjective_2, adjective_3, noun_1):
    # This definition should take in 4 strings, format them into the string below, and print the final string.
    text = 'The {} man entered the {} building to visit a very {} man. ' \
           'Sit down, Mr. Smith, can I interest you in any good {}?'.format(adjective_1).format(adjective_2).format(adjective_3).format(noun_1)
    return text


# print(madlib('tall', 'nice', 'tall', 'cat food'))

x = "Malayalam"
# print(x[::-1])


def read_file(filename):
    with open(filename) as input_file:
        x = input_file.readline()
        print(x)

# read_file('line_example.txt')
#
# with open('line_example.txt', 'r') as infile:
#     for line in infile:
#         print(line)

# more on .readlines() - it reads the whole file into memory as a list
with open('line_example.txt', 'r') as infile:
    x = infile.readlines()
    print(type(x))
    print(x)

#     # this example is a good chance to talk about a common bug you may encounter
    print(x[0])  # where did \n go?
    assert x[0] == 'hello Mohan D Thazhathethil', "x[0] is not line 1, it is: {}".format(x[0])  # adding quotes can make all the difference!


def check_delimiter(filename):
    with open(filename) as input_file:
        header = input_file.readline()
        if header.count(',') > header.count('\t'):
            return ','
        elif header.count('\t') > header.count(','):
            return '\\t'
        else:
            None


