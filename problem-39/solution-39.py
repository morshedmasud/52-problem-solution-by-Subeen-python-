# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    arr = input()
    rev_len = 1
    # looping in  half length of 'arr'
    for i in range(len(arr)//2):
        # checking first index to last index. if not match then it's not palindrome.
        if arr[i] != arr[len(arr)-rev_len]:
            print("Sorry! it's not palindrome!")
            break
        rev_len += 1
    else:
        print("Yes! it's palindrome")
    x += 1
