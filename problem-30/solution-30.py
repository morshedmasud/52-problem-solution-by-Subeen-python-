# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    n = int(input())
    su = 0
    for k in range(1, n):
        # Finding dicisor of n
        if n % k == 0:
            su += k

    if n == su:
        print("Yes, %d is a perfect number" %n)
    else:
        print("No, %d is not a perfect number" %n)
    x += 1