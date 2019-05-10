# for a string of DNA (Only A, T, C  and G), return its reverse compliment  (A <--> T) and  (G <--> C)
def rev_compliment(dna):

    COMP = {'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C', 'N' : 'N'}
    new_string = ''
    for letter in dna:
        new_string = new_string + COMP[letter]
    return new_string[::-1]

# x = rev_compliment('ATCCGGAAA')

# prints the first n lines from a file AND returns them as a list
def first_n_lines(filename, n):
    list = []
    with open(filename, 'r') as input_file:
        count = 0
        for line in input_file:
            if count < n:
                print(line)
                count += 1
                list.append(line)
        return list

# another way using enumerate:
def first_n_lines1(filename, n):
    list = []
    with open(filename, 'r') as input_file:
        for idx,line in enumerate(input_file):
            if idx < n:
                print(line)
                list.append(line)
        return list
# line_example.txt
# print(first_n_lines1('line_example.txt', 2))

# prints the lines m through n from a file AND returns them as a list

def line_m_to_n(filename, m, n):
    list = []
    with open(filename) as input_file:
        for idx, line in enumerate(input_file):
            if (idx >= m) and (idx <=n):
                print(line)
                list.append(line)
        return list
# print(line_m_to_n('line_example.txt', 1,2))

# Reads in a CSV file and returns a list of all entries in column 1

def read_first_column(filename):
    column= []
    with open(filename) as input_file:
        for line in input_file:
            column.append(line.split(',')[0])
        return column
# print(read_first_column('csv_example.csv'))

# Reads in a file, and determines if the first line is splittable by commas, tabs, or None,
#     and returns either  ','   '\t'   or   None

def check_delimiter(file_name):
    with open(file_name) as input_file:
        first_line = input_file.readline()
        number_of_column_by_comma = first_line.split(',')
        number_of_column_by_tab = first_line.split('\t')
        if len(number_of_column_by_comma) > 0:
            return ','
        elif len(number_of_column_by_tab) > 0:
            return '\t'
        else:
            return None
print(check_delimiter('csv_example.csv'))

# Reads the CSV file, file_name, and returns a list of every row where the first item in that row is 'name'
    # for example, return a list of every row from csv_example.csv where the first column is 'banana'

def get_rows_by_name(file_name, name):
    list = []
    with open(file_name) as input_file:
        for line in input_file:
            x = line.split(',')[0]
            if x == name:
                list.append(line)
        return list

# print(get_rows_by_name('csv_example.csv', 'banana'))

    """
    Reads the CSV file, file_name, and return a dictionary where each row is an entry,
    the key should be the item in the m column, and the value should be the item in the n column
    For example, return a dictionary of the form {fruit_name: taste, ...} for each fruit in csv_example.csv
    """

def columns_to_dictionary(file_name, m, n):
    dict = {}
    with open(file_name) as input_file:
        for line in input_file:
            x = line.split(',')
            dict[x[m]] = x[n]
        return dict

print(columns_to_dictionary('csv_example.csv', 2,3))
