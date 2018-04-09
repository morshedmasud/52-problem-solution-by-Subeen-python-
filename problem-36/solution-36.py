# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    arr = []
    for i in range(int(input())):
        arr.append(input())
    print()
    for i in sorted(arr):
        print(i)
    print()
    x += 1
