
def reverse_complement(dna):
    new_string = ''
    COMP = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G', 'N' : 'N'}
    for letter in dna:
        new_string = new_string + COMP[letter]
    return new_string[::-1]

# print(reverse_complement('GGCCCTTAA'))

def array_to_string(arr):
    return ''.join(arr)

# print(array_to_string(['a','b','c','f']))

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


def translate_dna(dna):

    new_string = ''
    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]
        if len(codon) < 3:
            continue
        new_string = new_string + DNA_TO_AA[codon]
    return new_string

# print(translate_dna('ATGGGTGGGATAGTGTAG'))

def all_reading_frame_translations(dna):
    """
    returns 6 strings of amino acids that are possible from one strand of dna
    """
    first = dna
    second = dna[1:]
    third = dna[2:]

    rev = reverse_complement(dna)
    revfirst = rev
    revsecond = rev[1:]
    revthird = rev[2:]

    six_strings = [first, second, third, revfirst, revsecond, revthird]

    proteins = []
    for dna in six_strings:
        proteins.append(translate_dna(dna))

    return proteins
# print(all_reading_frame_translations('AAACCCGGGTTTGGGAACCCAAA'))

def fasta_dictionary(fasta_file):
    """
    returns a dictionary where each key/value pair is a header/sequence in the fasta file
    {">human": "AAACCCGGGTTT", ...}

    human [region=California] [age=50]
    AAACCCGGGTTT
    """
    fasta_dict = {}
    with open(fasta_file, 'r') as infile:
        all_text = infile.read()
    for entry in all_text.split('>')[1:]:
        entry = entry.split('\n', maxsplit=1)
        fasta_dict[entry[0].split()[0]] = entry[1].replace('\n', '')
    return fasta_dict

# print(fasta_dictionary('fasta_example.fasta'))

dict = {}
dict['k'] = 'v'
dict['k1'] = 'v1'


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

print(possible_proteins('AYKPMVVVYYYMP*MAA'))

