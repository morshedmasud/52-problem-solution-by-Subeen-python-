# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    a, b, c = map(int, input().split())
    # for loop step
    step = a * b
    for i in range(step, c+1, step):
        print(i)
    print()
    x += 1
