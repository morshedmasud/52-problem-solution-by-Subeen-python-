# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    # Create a function for return 'n' factorial
    def fact(n):
        temp = 1
        for i in range(1, n+1):
            temp *= i
        return temp
    n = int(input())
    total = 0
    for i in range(1, n+1):
        total += i / fact(i)
    print("%.4f \n" %total)
    x += 1