# Taking value of t from user for how many test case we want
t = int(input())
k = 1
# Loop for test case
while k <= t:
    # Taking value of n for it's Divisor
    n = int(input())
    # showing test case number
    print("Case %d: " %k, end='')
    i = 1
    # Loop for number divisor
    while i <= n:
        if n % i == 0:
            print(i, end=' ')
        i += 1
    k += 1
    print()