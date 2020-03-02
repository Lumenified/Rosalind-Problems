from Bio.Seq import Seq

def ReverseComplimentaryDNA():
    """
    A small tweak (reading and modifying the file).
    """
    with open("rosalind_revc.txt") as p:
        my_seq = p.readlines()
        seq = Seq(my_seq[0])
        return seq.reverse_complement()
print(ReverseComplimentaryDNA())
