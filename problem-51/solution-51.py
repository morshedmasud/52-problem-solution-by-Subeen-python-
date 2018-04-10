# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    st, sub = map(str, input().split())
    count = 0
    for i in range(0, len(st)):
        if st[i:i+len(sub)] == sub:
            print("%d \n" %i)
            break
        else:
            pass
    x += 1