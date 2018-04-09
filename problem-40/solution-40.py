# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    n, p = map(int, input().split())
    result = 0
    for i in range(p+1):
        # add 'n' power 'i' in result
        result += n**i
    print("Result = %d\n" %result)
    x += 1

