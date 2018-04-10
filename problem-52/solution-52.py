# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    st, sub = map(str, input().split())
    count = 0
    for i in range(0, len(st)):
        if st[i:i+len(sub)] == sub:
            count += 1
    print(count, "\n")
    x += 1