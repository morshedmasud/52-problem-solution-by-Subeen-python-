# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    arr_len = int(input("Input for arr lenght: "))
    arr = list(map(int, input().split()))
    for i in range(0, len(arr), 2):
        print(arr[i], end=' ')
    print()
    x += 1

