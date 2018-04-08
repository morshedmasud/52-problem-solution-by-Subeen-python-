# Taking value of 'n' for test case
t = int(input())
x = 0
while x < t:
    # Taking value of 'n' from user
    n = int(input())
    fact = 1
    # Loop for multiply every value of 'i' by running value of 'fact'
    for i in range(2, n+1):
        fact = fact * i
    print(fact, "\n")
    x += 1