import math
# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    # Taking input from user for number range
    m, n = map(int, input().split())
    count = 0
    for i in range(m, n+1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            # if 'i' is prime then add 1 in count
            else:
                count += 1
    print(count, "\n")
    x += 1