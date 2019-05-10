"""
This document was written during class from the questions asked,
it is not a list of topics or questions chosen by me.

If this document is empty, no one asked any questions

"""

def check_delimiter(file_name):
    """
    Reads in a file, and determines if the first line is splittable by commas, tabs, or None,
    and returns either  ','   '\t'   or   None
    """
    with open(file_name, 'r') as infile:
        line = infile.readline()
    if line.count(',') > line.count('\t'):
        return ','
    elif line.count(',') < line.count('\t'):
        return '\t'
    else:
        return None








def vcf_region(vcf_file, m, n):
    """
    return a list of every row in the VCF file where POS (position) is between m and n
    EX: m=10000, n=200000 and the example VCF file will return a list of the elements:
    20     14370   rs6054257 G      A       29   PASS   NS=3;DP=14;AF=0.5;DB;H2           GT:GQ:DP:HQ 0|0:48:1:51,51 1|0:48:8:51,51 1/1:43:5:.,.
    20     17330   .         T      A       3    q10    NS=3;DP=11;AF=0.017               GT:GQ:DP:HQ 0|0:49:3:58,50 0|1:3:5:65,3   0/0:41:3
    """
    newl = []
    with open(vcf_file, 'r') as infile:
        for line in infile:
            if line.startswith('#'):
                continue
            line = line.strip().split()
            if int(line[1]) > m and int(line[1]) < n:
                newl.append(','.join(line) + '\n')
    return newl


def check_duplicates(fasta_file):
    """
    returns a list of headers that are present multiple times within a file
    """
    headers = []
    with open(fasta_file, 'r') as infile:
        for line in infile:
            if line.startswith('>'):
                headers.append(line)


    for header in set(headers):
        if header in headers:
            index = headers.index(header)
            headers.pop(index)

    return list(set(headers))



def no_compliments(fastq_file):
    """
    check every sequence in the FASTQ file to see if its reverse compliment is already in the file
    **FASTQ files are typically much larger than FASTA files, be sure to use the correct data structures
    return True if no duplicates exist, return False otherwise
    """

    seqs = set()
    header = None
    with open(fastq_file, 'r') as infile:
        for idx, line in enumerate(infile):
            line = line.strip()
            if idx%4 == 0:
                header = line
            if idx%4 == 1:
                seq = line
                if rev_comp(seq) in seqs:
                    return False
                seqs.add(rev_comp(seq))
                seqs.add(seq)
    return True



def split_x_y(mylist, x, y):
    """
    return all elements between the occurrences of element x and element y in mylist
    """
    position_x = mylist.index(x)
    position_Y = mylist.index(y)

    return mylist[position_x:position_Y]