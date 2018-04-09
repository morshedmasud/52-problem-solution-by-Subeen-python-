import math
# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    x1, y1 = map(int, input().split())
    r = int(input())
    x2, y2 = map(int, input().split())
    c = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if c > r:
        print("The point is not inside the circle")
    else:
        print("The point is inside the circle")
    x += 1