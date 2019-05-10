"""
Practice Problems 5

This is a collection of problems from the previous practice problems that can use Comprehension in some way.
In addition to this, it would be helpful to be able to solve all of exam 1 in list comprehension!


Using comprehension on all of these problems is possible, but may be less effective on some problems - especially those that return booleans
These problems do NOT need to be solved in one line. (but many of them can be!)
"""


def first_ten(my_list):
    """
    return a list of the first 10 elements in my_list
    """
    return

print(first_ten([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))


def last_ten(my_list):
    """
    return a list of the last 10 elements in my_list
    """
    return


def every_second(my_list):
    """
    return a list of the every second element
    """
    return

def count_letters(my_string):
    """
    return a dictionary where keys are letters in my_string, and values are the number of times that letter has occurred
    """
    return


def add_words(my_list, my_dict):
    """
    add each object in my_list to my_dict, where the key is the object, and the value is the number of times that object has occurred
    """
    return

def overlap(x, y):
    """
    Given two lists, x and y, return a new list of all elements that are in both lists
    """
    return


def only_x(x, y):
    """
    Given two lists, x and y, return a new list of all elements that are ONLY found in x
    """

    return

def rev_compliment(dna):
    """
    for a string of DNA (Only A, T, C  and G), return its reverse compliment  (A <--> T) and  (G <--> C)
    """
    return



def transcribe(dna):
    """
    DNA is converted to RNA through transcription, transcribe the string of DNA to RNA
    (the string is given 5' -> 3' and your result should be read 5' -> 3')
    EX: transcribe('CTGATCAG') returns 'CUGAUCAG'
    """
    return

def first_column(file_name):
    """
    Reads in a CSV file and returns a list of all entries in column 1
    """
    return

def get_rows_by_name(file_name, name):
    """
    Reads the CSV file, file_name, and returns a list of every row where the first item in that row is 'name'
    for example, return a list of every row from csv_example.csv where the first column is 'banana'
    """
    return



def columns_to_dictionary(file_name, m, n):
    """
    Reads the CSV file, file_name, and return a dictionary where each row is an entry,
    the key should be the item in the m column, and the value should be the item in the n column
    For example, return a dictionary of the form {fruit_name: taste, ...} for each fruit in csv_example.csv
    """
    return



def fasta_headers(file_name):
    """
    return a list of headers for the FASTA file
    """
    return



def fastq_headers(file_name):
    """
    prints a list of headers for reads in the FASTQ file
    """
    return



def fasta_sequences(file_name):
    """
    returns a list of sequences in a fasta file
    """
    return



def fasta_overlap(fasta_one, fasta_two):
    """
    returns a list of headers that are present in both fasta files
    """
    return



def fasta_dictionary(fasta_file):
    """
    returns a dictionary where each key/value pair is a header/sequence in the fasta file
    {">human": "AAACCCGGGTTT", ...}
    """
    return



def check_duplicates(fasta_file):
    """
    returns a list of headers that are present multiple times within a file
    """
    return



def vcf_header(vcf_file):
    """
    return the entire header sequence of a VCF file (the header region is the section where every line starts with ##)
    """
    return


def no_compliments(fasta_file):
    """
    check every sequence in the FASTA file to see if it's reverse compliment is already in the file
    return True if no compliments are present, return False otherwise
    """
    return