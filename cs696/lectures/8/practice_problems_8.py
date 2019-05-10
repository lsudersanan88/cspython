"""
Write your own class that will match the usage cases at the bottom of the file
"""

class FastaReader:
    pass










# --------- Usage cases, with assert statements ------------
# Uncomment the next 2 lines to generate example.fasta:
# with open('example.fasta', 'w') as outfile:
#     outfile.write('\n'.join(['>header1', 'seq1', '>header2', 'seq2', '>header3', 'seq3', '>header4', 'seq4']))



ff = FastaReader('example.fasta')

x = ff.to_dict()
assert x == {'>header1': 'seq1', '>header2': 'seq2', '>header3': 'seq3', '>header4': 'seq4'}

x = ff.headers
assert x == ['>header1', '>header2', '>header3', '>header4']

x = ff.get_headers(2)  # returns the first n headers
assert x == ['>header1', '>header2']

x = ff.seqs
assert x == ['seq1', 'seq2', 'seq3', 'seq4']

x = ff.get_seqs(3)
assert x == ['seq1', 'seq2', 'seq3']

x = len(ff)
assert x == 4

x = str(ff)
assert x == 'example.fasta'




