with open("rosalind_gc.txt", "r") as p:
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
                my_file.append([my_id,my_cache])
                my_id = i[1:]
                my_cache = ""
        else:#if the line doesnt start with the symbol it means its our gene's itself or extent
            my_cache += i[:-1]#we add up the nucleotide lines until \n (end of a line)
        pass
    my_file.append([my_id, my_cache])

def calc_gc_content(seq):
    """
        its calculating the G/C content and returns the id and its ratio as n (unlike n/100)
    """
    mylist = []
    for j in range(len(seq)):
        my_ratio = (seq[j][1].count("G") + seq[j][1].count("C"))/len(seq[j][1]) * 100
        mylist.append([seq[j][0], my_ratio])
        pass
    my_return = sorted(mylist, key=lambda x: x[1], reverse=True)
    return str(my_return[0][0]) + str(my_return[0][1])
print(calc_gc_content(my_file))
