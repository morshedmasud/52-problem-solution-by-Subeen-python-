# Taking value of 't' from user for test case
t = int(input())
x = 1
while x <= t:
    # Taking value of 'n1', 'n2', 'n3' from user.
    n1, n2, n3 = map(int, input().split())
    if n1 > n2:
        n1, n2 = n2, n1
        if n2 > n3:
            n2, n3 = n3, n2
            if n1 > n2:
                n1, n2 = n2, n1
    if n1 > n3:
        n1, n3 = n3, n1
    elif n2 > n3:
        n2, n3 = n3, n2
    print("Case %d : %d %d %d" %(x, n1, n2, n3), "\n")
    x += 1