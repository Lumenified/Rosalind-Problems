with open("tuts7.txt") as f:
    my_file = [int(i) for i in str(f.read()).split()]
    d = my_file[0]#Dominants
    h = my_file[1]#Hetero
    r = my_file[2]#Recessive

def MendelFzero(dominant: int, hetero: int, recessive: int):
    """
    takes 3 integers
    returns F0 crosses
    """
    pop = []
    pop += ["AA" for i in range(dominant)]
    pop += ["Aa" for i in range(hetero)]
    pop += ["aa" for i in range(recessive)]
    cross = []
    j = 0
    for i in pop:
        j += 1
        for k in pop[j:]:
            cross.append([i,k])
    return cross

def MendelFone(mylist: dict):
    """
    takes dict
    returns F1 generation
    """
    crossed = []
    for i in mylist:
        for j in i[0]:
            first_allel = j
            for k in i[1]:
                second_allel = k
                crossed.append(j+k)
    return crossed

def dominant_ratio(my_array: dict):
    """
    takes dict
    returns phenotypic dominant individuals' and its ratio as tuple
    """
    dominantNumber = 0
    for i in my_array:
        if str(i).__contains__("A"):
            dominantNumber +=1
    return float(dominantNumber/len(my_array))

myFzero = MendelFzero(d, h, r)
#print(len(myFzero))
myFone = MendelFone(myFzero)
#print(len(myFone))
print(dominant_ratio(myFone))
