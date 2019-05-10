"""
Practice problems 3:

Reading File Types

NOTE: if this is your first time working with file paths, you may get a
 FileNotFoundError: [Errno 2] No such file or directory: 'my_folder/myfile.txt'
If you are sure the file exists, then you are entering the wrong path to your file.

For example: data/example_1.fasta will look for a folder called 'data' in the same directory as your python script,
once it has found the folder 'data' it will look inside for a file called 'example_1.fasta'
If you do not have a folder called 'data' next to your python script, you will get an error
If you do not have a file called 'example_1.fasta' in that folder, you will get an error
"""


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



def possible_proteins(amino_acids):
    """
    for a string of amino acids (using one letter codes), return a list of possible proteins
    (proteins can start at any Methionine (M) and end at the first stop codon (*) )
    EX: AYKPMVVVYYYMP*MAA  will have only two possible proteins:
    MVVVTTTMP*   and    MP*
    """
    return



def first_n_lines(file_name, n):
    """
    prints the first n lines from a file AND returns them as a list
    """
    return



def lines_m_to_n(file_name, m, n):
    """
    prints the lines m through n from a file AND returns them as a list
    """
    return



def first_column(file_name):
    """
    Reads in a CSV file and returns a list of all entries in column 1
    """
    return



def check_delimiter(file_name):
    """
    Reads in a file, and determines if the first line is splittable by commas, tabs, or None,
    and returns either  ','   '\t'   or   None
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



def fastq_headers(file_name, n):
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



def vcf_region(vcf_file, m, n):
    """
    return a list of every row in the VCF file where POS (position) is between m and n
    EX: m=10000, n=200000 and the example VCF file will return a list of the elements:
    20     14370   rs6054257 G      A       29   PASS   NS=3;DP=14;AF=0.5;DB;H2           GT:GQ:DP:HQ 0|0:48:1:51,51 1|0:48:8:51,51 1/1:43:5:.,.
    20     17330   .         T      A       3    q10    NS=3;DP=11;AF=0.017               GT:GQ:DP:HQ 0|0:49:3:58,50 0|1:3:5:65,3   0/0:41:3
    """
    return



def no_compliments(fasta_file):
    """
    check every sequence in the FASTA file to see if it's reverse compliment is already in the file
    return True if no compliments are present, return False otherwise
    """
    return



def no_compliments(fastq_file):
    """
    check every sequence in the FASTQ file to see if its reverse compliment is already in the file
    **FASTQ files are typically much larger than FASTA files, be sure to use the correct data structures
    return True if no duplicates exist, return False otherwise
    """
    return




