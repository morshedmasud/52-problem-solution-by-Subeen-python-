# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    # Taking value of 'n' from user for sum
    n = int(input())
    # lsd for last digit
    lsd = n % 10
    while n > 0:
        # msd for first digit
        msd = n % 10
        temp = n // 10
        n = temp
    print("Sum =",(lsd+msd),"\n")
    x += 1g
