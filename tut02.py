
with open("rosalind_rna.txt") as f:
    modified = f.readlines()[0]
    mylist = "".join([str(x) if not x=="T" else"U" if not x=="\n" else "" for x in modified])
print(mylist)
