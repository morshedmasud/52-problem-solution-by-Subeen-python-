# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    # Taking string from user for 's'
    s = input()
    for i in s:
        if i >= 'A' and i <= 'Z':
            print(ord(i)-64, end='')
    print('\n')
    x += 1