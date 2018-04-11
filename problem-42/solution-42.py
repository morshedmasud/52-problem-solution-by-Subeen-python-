# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    n = int(input())
    # create a reversed loop
    for i in range(n, 0, -1):
        if i == 1:
            print("%d\n" %i)
        elif i == 2:
            print("%d + " %i, end='')
        else:
            print("2^%d + " %i, end='')
    x += 1