# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    # Taking value of 'string' and also make a list using 'split' function
    string = input().split()
    count += 1
    # count every word in string and increce count value.
    for i in string:
        count += 1
    print("Count = %d \n" %count)
    x += 1