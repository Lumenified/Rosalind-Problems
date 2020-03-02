
with open('rosalind_dna.txt') as f:
    myfile = f.readlines()
print(myfile[0].count("A"), myfile[0].count("C"), myfile[0].count("G"), myfile[0].count("T"))
