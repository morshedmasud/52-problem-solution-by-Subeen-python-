# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    n = int(input())
    if n >= 2:
        check = 1
        for i in range(2, n):
            if n % i == 0:
                check = 0
                break
    if check:
        print("%d is a prime number\n" %n)
    else:
        print("%d is not a prime number\n" %n)
    x += 1