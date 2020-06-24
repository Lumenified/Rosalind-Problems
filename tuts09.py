myfile = open("rosalind_subs.txt").readlines()
result = "".join([str(i + 1) + " " for i in range(len(myfile[0].rstrip("\n"))-len(myfile[1].rstrip("\n"))) if myfile[0].rstrip("\n")[i:i+len(myfile[1].rstrip("\n"))] == myfile[1].rstrip("\n")])    
print(result)

