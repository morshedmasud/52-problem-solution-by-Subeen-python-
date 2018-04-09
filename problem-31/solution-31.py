# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    n = int(input())
    count = 0
    for k in range(1, n+1):
        s = 0
        for i in range(1, k):
            count += 1
            if k % i == 0:
                s += i
        if s == k:
            print(k)
    print()
    x += 1