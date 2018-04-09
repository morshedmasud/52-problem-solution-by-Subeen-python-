# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    n = float(input("Enter float type number: "))
    count = 0
    while n > 1:
        n = n / 2
        count += 1
    print("%d days\n" %count)
    x += 1