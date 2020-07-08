### NOT COMLPETED!
seq = []

with open("testfile.txt", "r") as f:
    seq_id = ""
    cache_string = ""
    for line in f:
        if line[0] == ">":
            if cache_string is "":
                seq_id = line[1:].rstrip()
            else:
                seq.append([seq_id, cache_string])
                cache_string = ""
                seq_id = line[1:].rstrip()
        else:
            cache_string = cache_string + line.rstrip()
    seq.append([seq_id, cache_string])
#print(seq)

from collections import deque

mylist = deque(seq)
mylist.rotate(1)
print(mylist)
