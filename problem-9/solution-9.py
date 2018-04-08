import math
# Taking value of 't' from user for test case.
t = int(input())
x = 0
while x < t:
    # Taking value of 'n'
    n = int(input())
    # Using sqrt() for find sqrt
    sq = math.sqrt(n)
    if sq * sq == n:
        print("YES \n")
    else:
        print("NO \n")
    x += 1