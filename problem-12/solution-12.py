import math
# Taking value of 't' for test case
t = int(input())
x = 0
while x < t:
    # Taking value of 'n' from user
    n = int(input())
    fact = 1
    # Loop for multiply every value of 'i' by running value of 'fact'
    for i in range(2, n+1):
        fact = fact * i
    count = 0
    while fact > 0:
        mod = fact % 10
        if mod == 0:
            count += 1
        else:
            break
        fact = fact // 10
    print(count, "\n")
    x += 1