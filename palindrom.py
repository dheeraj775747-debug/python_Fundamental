str=input("Enter a string: ")
left=0
right=len(str)-1
while left < right:
    if str[left] != str[right]:
        print("The string is not a palindrome.")
        break
    left += 1
    right -= 1
else:
    print("The string is a palindrome.")