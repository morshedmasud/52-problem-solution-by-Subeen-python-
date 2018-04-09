# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    word = input()
    # Reversed loop
    for i in range(len(word)-1 , -1, -1):
        # showing reversed index of word
        print(word[i], end='')
    print('\n')
    x += 1