# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    n, l = map(int, input().split())
    for i in range(1, n+1):
        print(str(l) * i)
    for j in range(n-1, 0, -1):
        print(str(l) * j)
    print()
    x += 1