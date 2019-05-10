def duplicate_headers(fasta_file):
    """
    Given a fasta file, check to see if there are any duplicate headers, return True if there are, False otherwise
    :param fasta_file: a text file in the FASTA file
    :return: boolean, True or False
    """
    all_headers = []
    with open(fasta_file) as input_file:
        for line in input_file:
            line = line.strip()
            print(line)
           # if line.startswith('>'):
               # all_headers.append(line.replace('\n', '').replace('>',''))
       # if len(all_headers) > len(set(all_headers)):
           # return True
        #else:
           # return False

print(duplicate_headers('fasta_example.fasta'))

# assert duplicate_headers('fasta_example.fasta') == False, "Try problem 6 again"
# Uncomment the following line to generate the test file: "fasta_example.fasta"
with open('fasta_example.fasta', 'w') as outfile: [outfile.write(line) for line in ['>human\n', 'AAACCCGGGTTT\n', '>corn\n', 'GGGTTTAAACC\n', 'CCCGGGTTTAA\n', '>cat\n', 'CATCAT\n', '>cat\n', 'CATCATCATCATCATCATCATCATCATCATCATCATCATCATCAT\n']]
