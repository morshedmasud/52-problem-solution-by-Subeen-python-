# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    n = int(input())
    rev = 0
    while n != 0:
        rev = rev * 10
        rev += n % 10
        n = n // 10
    print(rev, "\n")
    x += 1