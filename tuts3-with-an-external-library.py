from Bio.Seq import Seq

def ReverseComplimentaryDNA():
    """
    A small tweak (reading and modifying the file).
    """
    with open("rosalind_revc.txt") as p:
        seq = Seq(p.readlines()[0])
        return seq.reverse_complement()
print(ReverseComplimentaryDNA())
