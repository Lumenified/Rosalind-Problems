from Bio import SeqIO

mypool = [] #my gene pool

for record in SeqIO.parse("./myfile.txt", "fasta"):
    mypool.append(record)

DoIGenes = []# a dict of individual genes

for i in range(len(mypool)):
    DoIGenes.append([mypool[i].id ,(list(mypool[i]).count("G")+list(mypool[i]).count("C"))/len(mypool[i])*100])

HGCContent = sorted(DoIGenes,reverse=True)[0] # The highest GC content
print(HGCContent[0])
print(HGCContent[1])
