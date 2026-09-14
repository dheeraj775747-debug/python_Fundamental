# move non zero to right most [1,,0,2,0,0,1,0]
arr = [1,0,2,0,0,1,0]

# slow pointer starts at index 0
slow = 0 
# Fast pointer visit every index from left to right 
for fast in range (len(arr)):

# Check if the current element is NOT zero 
    if arr [fast] != 0:
        # swap the non-zero element with the element at slow pointer
        arr[slow], arr[fast], = arr[fast], arr[slow]

# move slow pointer one position forward 
        slow += 1
        
# print the final array
print(arr)
    