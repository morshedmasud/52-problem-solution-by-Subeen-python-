# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    n = int(input())
    temp = n
    sum_n = 0
    while temp != 0:
        rem = temp % 10
        sum_n += (rem*rem*rem)
        temp = temp // 10

    if n == sum_n:
        print(n, "is an armstrong number! \n")
    else:
        print(n, "is not an armstrong number! \n")
    x += 1