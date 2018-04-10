# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    n_len, n = int(input("Input for n_length: ")), list(map(int, input().split()))
    for i in range(1, n_len+1):
        if i not in n:
            print(i, "\n")
            break
    x =+1

