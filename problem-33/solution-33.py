# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print(i)
    print()
    x += 1
