# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    m, n = map(int, input().split())
    if m >= n:
        print("Invalid!")
    else:
        for i in range(m, n+1, m):
            print(i)
    print()
    x += 1