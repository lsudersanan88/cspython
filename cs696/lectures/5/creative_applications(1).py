"""
Week 3

Creative uses for code we have learned so far

"""



# Reverse compliment without an if statement
def rev_comp(dna):
    """
    Given a string of DNA, return its reverse compliment  (A <-> T  and  C <-> G)
    """
    COMP = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'N': 'N'}
    new_string = ''
    for letter in dna:
        new_string = new_string + COMP[letter]
    print (new_string)
    return new_string[::-1]
#
print(rev_comp('CCGGTTTTAAAA'))



# Same concept, bigger dictionary
DNA_TO_AA = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W'}


def translate(dna):
    """
    return the string of amino acids coded for by the string dna
    """
    new_string = ''
    for i in range(0,len(dna),3):
        codon = dna[i:i+3]
        if len(codon) < 3:
            continue
        new_string = new_string + DNA_TO_AA[codon]
    return new_string

# print(translate('ATGGGTGGGATAGTGTAG'))



def all_reading_frame_translations(dna):
    """
    returns 6 strings of amino acids that are possible from one strand of dna
    """
    first = dna
    second = dna[1:]
    third = dna[2:]

    rev = rev_comp(dna)
    revfirst = rev
    revsecond = rev[1:]
    revthird = rev[2:]

    six_strings = [first, second, third, revfirst, revsecond, revthird]

    proteins = []
    for dna in six_strings:
        proteins.append(translate(dna))

    return proteins

# print(all_reading_frame_translations('AAACCCGGGTTTGGGAACCCAAA'))
# ['KPGFGNP', 'NPGLGTQ', 'TRVWEPK', 'FGFPNPG', 'LGSQTRV', 'WVPKPGF']


# remember, functions are objects and can be stored in dictionaries, this gives us a java 'switch' like statement
# in this example, every fruit needs to be processed differently, INSTEAD OF USING LOTS OF IF STATEMENTS, we can use a dictionary of defs
def process_orange(orange):
    return orange*2

def process_apple(apple):
    return apple*100

def process_banana(banana):
    return banana*-1

def process_other(other_fruit):
    return 'Fruit not found'

SWITCH_DICT = {'orange': process_orange, 'apple': process_apple, 'banana': process_banana}

# fruit_file = '../04_file_types/data/csv_Example.csv'
# with open(fruit_file, 'r') as infile:
#     header = infile.readline()
#     for line in infile:
#         line = line.strip().split(',')
#         fruit = line[0]
#         taste = int(line[1])
#         def_to_use = SWITCH_DICT.get(fruit, process_other)
#         result = def_to_use(taste)  # use SWITCH_DICT.get() to set a default case
#         print(result)




# Converting an array to a string
# dna = ['A', 'C', 'T', 'G', 'G', 'G', 'A']
# dna = ''.join(dna)
# print(dna)


# the same syntax is great for writing CSV/TSV files!!!!!!!!!!!!!
# lines_to_write = [['fruit', 'flavor', 'convenience', 'durability'], ['banana', '5', '5', '2'], ['apple', '3', '4', '5'], ['grapes', '4', '4', '2'], ['lemon', '1', '3', '4'], ['orange', '3', '3', '3'], ['watermelon', '4', '1', '5'], ['tomato', '2', '2', '1']]
# with open('fruit_ratings.csv', 'w') as outfile:
#     for line in lines_to_write:
#         outfile.write(','.join(line) + '\n')  # what went wrong?



## More on sets()
# Unique elements in a list? (removing duplicates)
# x = [0, 0, 1, 0, 1, 2, 1, 4, 6, 2, 1]
# x = list(set(x))
# print(x)



# # Lets look at some practice problems
def only_x(x, y):
    """
    Given two lists, x and y, return a new list of all elements that are ONLY found in x
    """
    return list(set(x) - set(y))

# x = [0, 1, 2, 3, 4]
# y = [3, 4, 5, 6, 7]
# print(only_x(x, y))



def overlap(x, y):
    """
    Given two lists, x and y, return a new list of all elements that are in both lists
    """
    return set(x).intersection(set(y))

# x = [0, 1, 2, 3, 4]
# y = [3, 4, 5, 6, 7]
# print(overlap(x, y))



# .split() isn't just for CSV files
def possible_proteins(amino_acids):
    """
    for a string of amino acids (using one letter codes), return a list of possible proteins
    (proteins can start at any Methionine (M) and end at the first stop codon (*) )
    EX: AYKPMVVVYYYMP*MAA  will have only two possible proteins:
    MVVVTTTMP*   and    MP*
    # careful using range(len())! len counts elements (1 based)
    """
    prots = []
    possible = amino_acids.split('*')
    if not amino_acids.endswith('*'):
        possible = possible[:-1]
    for p in possible:
        for idx, char in enumerate(p):
            if char == "M":
                prots.append(p[idx:])
    return prots

# print(possible_proteins('AYKPMVVVYYYMP*MAA'))


# another demonstration of .split()  and .read()
def fasta_dictionary(fasta_file):
    """
    returns a dictionary where each key/value pair is a header/sequence in the fasta file
    {">human": "AAACCCGGGTTT", ...}
    """
    fasta_dict = {}
    with open(fasta_file, 'r') as infile:
        all_text = infile.read()
    for entry in all_text.split('>')[1:]:
        entry = entry.split('\n', maxsplit=1)
        fasta_dict[entry[0].split()[0]] = entry[1].replace('\n', '')
    return fasta_dict

# print(fasta_dictionary('../04_file_types/data/fasta_example.fasta'))



## Use built-ins before paper clips and duct tape
# count how many Methionines (M) are in the protein:
# protein = 'MAGRGYMTMGMGG*'
# m_count = 0
# for char in protein:
#     if char == 'M':
#         m_count += 1
# print(m_count)
#
# # or
#
# print(protein.count("M"))


## But kyle, how am I supposed to know that .count() is available? what other built-in methods don't I know about?
# you have access to the documentation for all built in methods on the exam:

# all built-in methods called on strings
# print(help(def))

# how do I find out more about a method, like .replace()?
# print(help(str.replace))
# # or
# print(str.replace.__doc__)



