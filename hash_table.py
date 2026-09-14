arr = [30,34,32,55,60]
size = 10
hash_table = [None]*size
for num in arr:
    index = num % size 
    hash_table[index] = num 
    print(hash_table)