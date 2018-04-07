# Taking value of 't' from user.
t = int(input())
i = 0
while i < t:
    n = int(input())
    x = 0
    # showing n time's '*' every time of x
    while x < n:
        print('*' * n)
        x += 1
    i += 1
    print()
