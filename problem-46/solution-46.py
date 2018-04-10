import math
# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    m, p, n = map(int, input().split())
    s = (m + p + n) / 2
    area = math.sqrt(s * (s-m) * (s-p) * (s-n))
    print("Area = %.3f\n" %area)
    x += 1
