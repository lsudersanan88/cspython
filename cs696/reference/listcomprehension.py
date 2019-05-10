import math


def ceiling(my_list, max_value):
    """
    Return a list, where every element in my_list that is greater than the max_value, is reduced to max_value.
    EX: ceiling([1, 10, 100, 200, 300], 150) -> [1, 10, 100, 150, 150]
    """
    return [max_value if item > max_value else item for item in my_list]
#print(ceiling([1, 10, 100, 200, 300], 150))

def squish(my_list, min_value, max_value):
    """
    Return a list, where every element in my_list that is less than min_value is raised to min_value, AND
     every element that is greater than max_value is reduced to max_value.
    EX: squish([1, 10, 100, 200, 300], 15, 150) -> [15, 15, 100, 150, 150]
    """

    return[min_value if item < min_value else max_value if item > max_value else  item for item in my_list]


#print(squish([1, 10, 100, 200, 300], 15, 150))

def n_by_m_zeros(m, n):
    """
    Return a list of length m, where each element in m, is a list of 0's length n.
    EX: n_by_m_zeros(4, 2) -> [[0, 0], [0, 0], [0, 0], [0, 0]]
    """
    return [[0 for _ in range(0,n)] for _ in range(0,m)]
   # return [[(0) for inner_cnt in range(0,n)]for count in range (0,m)]

#print(n_by_m_zeros(4, 2))

def dict_low_pass(my_dict):
    """
    Return a dictionary of only the key/value pairs from my_dict whose value is GREATER THAN 10.
    EX: dict_low_pass({'a': 1, 'b': 10, 'c': 11}) -> {'c': 11}
    """
    #return {my_dict(k, v) for k, v in my_dict if v >= 10}
    #return {my_dict[value]:value for value  in my_dict if value > 10 }
    return {key:my_dict[key] for key in my_dict if my_dict[key]>10}
    #return {key: my_dict[key] for key in my_dict if my_dict[key] > 10}

#print(dict_low_pass({'a': 1, 'b': 10, 'c': 11}))

def shared_element_count(list_a, list_b):
    """
    Return an int representing the number of elements that are in both list_a and list_b
    EX: shared_element_count([1, 3, 5], [1, 2, 3]) -> 2
    """
    return[len(set(list_a).intersection(list_b))]
#print(shared_element_count([1, 3, 5], [6, 7, 8]))

def len_2_number_strings():
    """
    Return a list of strings (all length 2) representing all numbers '00' to '99'
    EX: len_2_number_strings() -> ['00', '01', '02', ... '98', '99']
    """
    return [ str(_).rjust(2, '0') for _ in range (0,99) ]

#print(len_2_number_strings())

def index_dict(my_list):
    """
    Return a dictionary where each key is an element in my_list and each value is the index of that element. There
     are no repeated elements in my_list.
    EX: index_dict(['name', 'id', 'age']) -> {'name': 0, 'id': 1, 'age': 2}
    """
   # return{my_list[value]:value for value in my_list}
    return {x:my_list.index(x) for x in my_list}
#print(index_dict(['name', 'id', 'age']) )

def absolute_average(my_list):
    """
    Return the average of the absolute values of all integers in my_list.
    EX: absolute_average([10, -10, 12, 12]) -> 11
    """
    #return [((sum(x) if x>0 else sum(-x)  ) for x in my_list)/len(my_list) ]
    return sum([x if x > 0 else x*-1 for x in my_list])/len(my_list)


#print(absolute_average([10, -10, 12, 12]) )

def specific_rows(filename, my_string):
    """
    Return a list of lines from filename that start with my_string
    EX: specific_rows('example.fastQ', '@') -> ['@srr_3403639', '@srr3403565', ...]
    """


# print(specific_rows('example.fastQ', '@'))

from math import log10
from math import log
def log10_row(my_list):
    """
    Return a list of the log10 of every value in my_list or '-' if the log cannot be taken.
    EX: log10([0, 1, 10 100]) -> ['-', 0.0, 1.0, 2.0]
    """
    return[log(y, 10) if y > 0 else '-' for y in my_list]

#print(log10_row([0, 1, 10, 100]) )

def log10_csv(list_of_lists):
    """
    Given a list containing lists, convert every value contained within to its log10 transformation or '-' if
     it is not possible. DO THIS WITHOUT CALLING THE log10_row() DEFINITION.
    EX: log10_csv([[0, 1, 10 100], [0, 1, 10 100]]) -> [['-', 0.0, 1.0, 2.0], ['-', 0.0, 1.0, 2.0]]
    """


# print(log10_csv([[0, 1, 10, 100], [0, 1, 10, 100]]))








def dict_low_pass(my_dict):
    """
    Return a dictionary of only the key/value pairs from my_dict whose value is GREATER THAN 10.
    EX: dict_low_pass({'a': 1, 'b': 10, 'c': 11}) -> {'c': 11}
    """
    return {key:my_dict[key] for key in my_dict if my_dict[key]>10}
#print(dict_low_pass({'a': 1, 'b': 10, 'c': 11,'d': 12, 'e': 21}))


def reverse_compliment(dna):

    new_string = ''
    comp = {'A':'T','T':'A','C':'G','G':'C'}
    for i in dna:
        new_string = new_string + comp[i] 
    return new_string[::-1]

print(reverse_compliment("AAACCCTGTG"))



































