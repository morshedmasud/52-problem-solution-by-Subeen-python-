# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    a = input()
    a = list(a)
    for i in range(len(a)):
        if a[i] == 'L':
            a[i] = a[i-1]
        elif a[i] == 'R':
            a[i] = a[i+1]
    print("".join(a), "\n")

    x += 1