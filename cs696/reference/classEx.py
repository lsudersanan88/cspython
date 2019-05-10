#write a file containing the FastaReader class, uncomment and run the next two lines
with open('fasta_reader2.py', 'w') as outfile:
     outfile.write('\n'.join(['import os', '', '', 'COMP_DICT = {"A": "T", "T": "A", "C": "G", "G": "C"}', '', 'class FastaReader:', '    """', '    THIS IS THE FastaReader DOCSTRING', '    """', '', '    def __init__(self, fname):', '        self.name = fname', '        if os.path.isdir(fname):', '            files = [os.path.join(fname, x) for x in os.listdir(fname)]', '        else:', '            files = [fname]', '        self.lines = []', '        for f in files:', '            self.lines += [x.strip() for x in open(f)]', '        self.lines = _clean_lines(self.lines)', "        self.headers = [x for x in self.lines if x.startswith('>')]", "        self.seqs = [x for x in self.lines if not x.startswith('>')]", '', '    def to_dict(self):', '        return {h:s for h,s in zip(self.headers, self.seqs)}', '', '    def get_headers(self, n):', '        return self.headers[:n]', '', '    def get_seqs(self, n):', '        return self.seqs[:n]', '', '    def __str__(self):', '        return self.name', '', '    def __len__(self):', '        return len(self.headers)', '', '    def rev_complement_seqs(self):', '        """', '        :return: a list of all reverse complemented sequences in the FASTA file', '        """', '        return [rev_complement(x) for x in self.seqs]', '', 'def rev_complement(seq):', '    """', '    Returns the complement of a sequence', '    """', "    return ''.join([COMP_DICT[x] for x in seq][::-1])", '', 'def _clean_lines(lines):', '    """', '    if the lines of a FASTA file do not alternate sequence and header,', '    then concatenate all sequences between each header and return a list of the new lines', '    (Remember, the "_" Underscore at the beginning of a definition means it is intended to', "      be 'private', but nothing is really 'private' in python -", '      see https://mail.python.org/pipermail/tutor/2003-October/025932.html for a laugh)', '    """', '    # this is a verbose solution with decent time', '    new_lines = []', "    seq = ''", '    header = None', '    for line in lines:', "        if line.startswith('>'):", '            if seq:', '                new_lines.append(header)', '                new_lines.append(seq)', "                seq = ''", '            header = line.rstrip()', '        else:', '            seq += line.rstrip()', '    new_lines.append(header)', '    new_lines.append(seq)', '', '    return new_lines']))
#
# # To write an example FASTA file, uncomment the next two liens
with open('example.fasta', 'w') as outfile:
    outfile.write('\n'.join(['>header1', 'AAACT', '>header2', 'CCCGT', '>header3', 'GGGTA', '>header4', 'TTTAG']))


from fasta_reader2 import FastaReader
import argparse
import sys
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('input', action="store")
    parser.add_argument('doc', action="store")
    parser.add_argument('comp', action="store")
    # parser.add_argument('-input', '--input', help='Input', required=True)
    # parser.add_argument('-doc', '--output', help='Output')
    try:
        args = parser.parse_args()
    except:
        print('Exception while parsing the argument')
        # parser.print_help()
        # sys.exit(1)
    if args.input == None:
        sys.exit(1)
    fasta_reader = FastaReader(args.input)
    if args.doc != None:
        print(fasta_reader.__doc__)