# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    n = []
    ch = 1
    # Input values of 'n' list
    for _ in range(int(input())):
        n.append(int(input()))

    for i in range(1, len(n)):
        if n[i] < n[i-1]:
            ch = 0
            break
    if ch:
        print("YES")
    else:
        print("NO")
    x += 1