# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    # Input from a sentence and make e list by split fuction
    word = input().split()
    for i in word:
        # Reversed every word and print.
        print(i[::-1], end=' ')
    print("\n")
    x += 1