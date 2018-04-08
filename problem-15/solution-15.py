# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    # Input from user or word
    n = input()
    count = 0
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i in n:
            print(i, "=", n.count(i))
    print()
    x += 1