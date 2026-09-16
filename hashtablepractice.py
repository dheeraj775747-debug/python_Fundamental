arr = [23,43,13,27,37]
size = 10
hash_table = [None]*size
for num in arr:
    index = num%size
    while hash_table[index] is not None:
        index = (index+1) % size
    hash_table[index] = num 
print(hash_table)