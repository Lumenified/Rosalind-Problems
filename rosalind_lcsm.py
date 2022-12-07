with open("rosalind_lcsm.txt", "r") as p:
    """
    modifying the fasta file.
    """
    my_file = []
    my_id = ""
    my_cache = ""
    my_gen = 0
    for i in p.readlines():
        if i[0] == ">":# ">" (bigger than) symbol indicates that its the id of our sequence
            if my_gen==0:
                my_id = i[1:]#without the symbol
                my_gen += 1
            else:
                my_file.append([my_id.replace("\n", ""),my_cache.replace("\n", "")])
                my_id = i[1:]
                my_cache = ""
        else:#if the line doesnt start with the symbol it means its our gene's itself or extent
            my_cache += i[:-1]#we add up the nucleotide lines until \n (end of a line)
    my_file.append([my_id.replace("\n", ""), my_cache.replace("\n", "")])
def motif(seq):
    seq_lengths = []
    for i in seq:
        seq_lengths.append([i[1] ,len(i[1]), seq.index(i)])
    seq_lengths.sort(key=lambda x:x[1])
    seq1 = seq[seq_lengths[0][2]][1]
    seq.pop(seq_lengths[0][2])
    for j in range(len(seq1), 5, -1):
        for k in range(len(seq1)-j+1):
            for i in seq:
                if seq1[k:k+j] in i[1]:
                    #print("attempt")
                    if i==seq[-1]:
                        return (seq1[k:k+j])
                else:
                    break