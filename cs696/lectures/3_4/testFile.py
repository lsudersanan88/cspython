tsv_file = 'data/tsv_example.tsv'
with open (tsv_file) as  infile:
    header = infile.readline().strip()
    split_header = header.split('\t')
    #print(header)
    list =[]
    for line in infile:
        line = line.strip().split('\t')
        list.append(line)
    print(list)
