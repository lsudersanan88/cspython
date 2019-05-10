"""
File Types


"""



## Opening files with open()

# The best way to read a file in python
# with open('data/line_example.txt', 'r') as input_file:
#     x = input_file.readline()  # reads the first line from "input_file"
#     print(x)
#
# print('file is now closed')  # when the 'with' indentation ends, the file is automatically closed!


# If you would rather do it the full manual way (not recommended)
# input_file = open('data/line_example.txt', 'r')
# x = input_file.readline()
# print(x)
# input_file.close()  # the file must be closed manually.


# open() can have many uses in python, here is a truncated output from
# print(help(open))    # or use: print(open.__doc__)
"""
open(file, mode='r')  # there are more arguments that can be passed to open(), but we wont use them
    Open file and return a stream.  Raise OSError upon failure.
    
    file is either a text or byte string giving the name (and the path
    if the file isn't in the current working directory). 
    
    mode is an optional string that specifies the mode in which the file
    is opened. It defaults to 'r' which means open for reading in text
    mode.  Other common values are 'w' for writing (truncating the file if
    it already exists), 'x' for creating and writing to a new file, and
    'a' for appending.
    
    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing: ERROR IF FILE EXISTS
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================
"""


# opening and writing a file
#with open('C:/Users/LS109949/Desktop/cs696/data/new_output.txt', 'w') as outfile:
with open('data/new_output.txt', 'w') as outfile:
 outfile.write('line1\nline2')


# opening the same file and appending to it
with open('data/new_output.txt', 'a') as outfile:
   outfile.write('\nline3\nline4')


# now look what happens when we open it with 'w' again; even if we dont write anything new
#with open('data/new_output.txt', 'w') as outfile:
    #print('the file has been opened again and has been overwritten')


# you can even open two files in a single statement:
with open('data/line_example.txt', 'r') as infile, open('data/new_output.txt', 'w') as outfile:
    x = infile.readline()
    outfile.write(x)



## Looping over files

# This is the best way, to loop over 'infile'
#with open('data/line_example.txt', 'r') as infile:
    #for line in infile:
         #print(line)


# sometimes you will see a loop over 'infile.readlines()', this is usually a bad practice
#with open('data/line_example.txt', 'r') as infile:
    #for line in infile.readlines():
        # print(line)


# more on .readlines() - it reads the whole file into memory as a list
# with open('data/line_example.txt', 'r') as infile:
#     x = infile.readlines()
#     # print(type(x))
#     # print(x)
#
#     # this example is a good chance to talk about a common bug you may encounter
#     # print(x[0])  # where did \n go?
#     # assert x[0] == 'line 1', "x[0] is not line 1, it is: {}".format(x[0])  # adding quotes can make all the difference!


# infile is like a generator, it only knows one value at a time, and only goes forward, no repeating
# (also, watch out for newline characters \n)!
# with open('data/line_example.txt', 'r') as infile:
#     header = infile.readline()
#     print('header is "{}"'.format(header))
#     for line in infile:
#         print(line)


# this is the same example as above, but we're going to introduce .strip()
#with open('data/line_example.txt', 'r') as infile:
    #header = infile.readline().strip()  # strip whitespace and newline from end of each line
    #print('header is "{}"'.format(header))
#     for line in infile:
#         print(line.strip())  # strip whitespace and newline from end of each line



## Now lets talk about reading in file types: no modules!

# first, the most common type of file we will see, a CSV file (comma separated values). Think of it as a spreadsheet where each comma starts a new cell
csv_file = 'data/csv_example.csv'
with open(csv_file, 'r') as infile:
    header = infile.readline().strip()
    split_header = header.split(',')  # split the string into a list, where each split happens at a comma
    #print("Old header: {}\nSplit Header: {}".format(header, split_header))
#for line in infile:
    #line = line.strip().split(',')  # always strip before you split!  (no jokes)
#print(line)


# TSV files are the same as CSV, but use tabs instead of commas ('\t' instead of ',')
tsv_file = 'data/tsv_example.tsv'
with open(tsv_file, 'r') as infile:
     header = infile.readline().strip()
     split_header = header.split('\t')  # split by the tab character
     print("Old header: {}\nSplit Header: {}".format(header, split_header))
#
     for line in infile:
         line = line.strip().split('\t')
     print(line)


# .FASTA files are the most common way to store sequence files, lets printing all sequence headers
# fasta_file = 'data/fasta_example.fasta'
# with open(fasta_file, 'r') as infile:
#     for line in infile:
#         line = line.strip()
#         if line[0] == '>':  # line[0] will evaluate to the first character in each line
#             print(line)
#
#         # why did this program fail?
#         # what if we used .startswith()?


# fastq files store sequences files AND their quality scores
# fasta_file = 'data/fastq_example.fastq'
# with open(fasta_file, 'r') as infile:
#     for line in infile:
#         line = line.strip()
#         if line.startswith('@'):
#             print(line)


# Variant Call Format (VCF): what variant of DNA is measured at a position
# For example sickle cell anemia is caused by a single T -> A, C, or G mutation on chromosome 11 at position 5,227,002 called rs344
# the shortest way to express this in VCF format is: 11  5227002  rs334  T  A,C,G
# more here: www.internationalgenome.org/wiki/Analysis/Variant Call Format/vcf-variant-call-format-version-40/
# and here:  https://en.wikipedia.org/wiki/Variant_Call_Format

# vcf_file = 'data/vcf_example.vcf'
# with open(vcf_file, 'r') as infile:
#     for line in infile:
#         line = line.strip().split()  # default split() will separate on all whitespace characters (spaces, tabs, newlines...)
#         if line[0] == 'X':
#             print(line)









