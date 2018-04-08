# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    # Taking words for 'n' from user
    n = input().split(' ')
    new_list = []
    n_len = 0
    for i in n:
        if i not in new_list:
            new_list.append(i)
            n_len += 1
    fact = 1
    for i in range(2, n_len+1):
        fact = fact * i
    print("1/%d \n" %fact)
    x += 1
