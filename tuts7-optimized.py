with open("tuts7.txt") as f:
    my_file = [int(i) for i in str(f.read()).split()]

def second_edit(pop: dict):
    return [1 - (( (pop[1])*(pop[2]) + .25*(pop[1])*((pop[1])-1) + (pop[2])*((pop[2])-1) ) / ( (pop[0]+pop[1]+pop[2])*((pop[0]+pop[1]+pop[2])-1) ))]

print(second_edit(my_file)[0])
