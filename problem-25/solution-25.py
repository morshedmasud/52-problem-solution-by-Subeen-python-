# Taking value of 't' from user for test case
t = int(input())
x = 0
while x <= t:
    a, b = map(int, input().split())
    # we use the logic in this code is (a gsd d * a lsd b = a * b)
    lsd = a * b
    # Finding gsd of a and b
    while b != 0:
        t = b
        b = a % b
        a = t
    lsd = lsd // a
    print("LSM = %d \n" %lsd)
    x += 1