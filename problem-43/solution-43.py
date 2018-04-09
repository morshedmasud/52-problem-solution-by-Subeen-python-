# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    p, q, c = map(int, input().split())
    # count q power of p
    p = p**q
    print("Result = %d \n" %(p % c))
    x += 1
