
def remove_duplicates(list1, list2):
    new_list = list(set(list1) - set(list2))
    return new_list

#print(remove_duplicates([1,2,3,4,5,6,9], [1,2,9]))

def check_delimiter(filename):
    with open(filename) as input_file:
        first_line = input_file.readline()
        if first_line.count(',') > first_line.count('\t'):
            return ','
        elif first_line.count('\t') > first_line.count(','):
            return '\\t'
        else:
            return None

# print(check_delimiter('csv_example.csv'))
# print(check_delimiter('tsv_example.tsv'))

def first_n_lines(file, n):
    list = []
    with open(file) as input_file:
        for idx,line in enumerate(input_file):
            if idx < n:
                list.append(line)

        return list

# print(first_n_lines('csv_example.csv',4))

# return a list of headers for the FASTA file
def fasta_headers(file_name):

    headers = []
    with open(file_name) as input_file:
        for line in input_file:
            if line.startswith('>'):
                headers.append(line)
        return headers

# print(fasta_headers('fasta_example.fasta'))

# prints a list of headers for reads in the FASTQ file

def fastq_headers(file_name):
    headers = []
    with open(file_name) as input_file:
        for line in input_file:
            line = line.strip()
            if line.startswith('@'):
                headers.append(line)
        return headers

# print(fastq_headers('fastq_example.fastq'))

# returns a list of sequences in a fasta file
def fasta_sequences(file_name):
    seqs = []
    with open(file_name) as input_file:
        for line in input_file:
            line = line.strip()
            if not(line.startswith('>')):
                seqs.append(line)
        return seqs

# print(fasta_sequences('fasta_example.fasta'))

# returns a dictionary where each key/value pair is a header/sequence in the fasta file

######################################### NOT CORRECT ########################################
def fasta_dictionary(fasta_file):
    dict = {}
    temp_count = 0
    key = ''
    with open(fasta_file) as input_file:
        for idx,line in enumerate(input_file):
            line = line.strip()
            if line.startswith('>'):
                key = line
                temp_count = idx
            elif idx == temp_count +1:
                dict[key] = line
        return dict


# print(fasta_dictionary('fasta_example.fasta'))

# returns a list of headers that are present multiple times within a file

def check_duplicates(fasta_file):
    with open(fasta_file) as input_file:
        headers = []
        for line in input_file:
            if line.startswith('>'):
                headers.append(line)
        unique_headers = set()
        duplicate_headers = []
        for header in headers:
            if header not in unique_headers:
                unique_headers.add(header)
            else:
                duplicate_headers.append(header)
        if duplicate_headers.count() > 0:
            duplicate_headers
        else:
            None