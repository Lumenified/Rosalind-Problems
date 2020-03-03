from Bio import SeqIO

mylist = []

for record in SeqIO.parse("./myfile.txt", "fasta"):
    mylist.append(record)

mycluster = []

for i in range(len(mylist)):
    mycluster.append([mylist[i].id ,(list(mylist[i]).count("G")+list(mylist[i]).count("C"))/len(mylist[i])*100])

print(sorted(mycluster,reverse=True)[0])
