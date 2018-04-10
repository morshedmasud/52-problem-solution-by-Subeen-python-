# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    n = int(input())
    lis = [1]
    # make a another list for nested list
    multi_list = []
    # Insert the first element in multio_list form lis
    multi_list.append(lis)
    for i in range(1, n+1):
        new_list = []

        new_list.append(lis[0])
        for j in range(len(lis)-1):
            new_list.append(lis[j] + lis[j+1])
        # Insert the last element in new_list form  lis
        new_list.append(lis[-1])
        lis = new_list
        multi_list.append(lis)
    for k in multi_list:
        print(' '.join(map(str, k)).center(n*3),'\n')
    x += 1
