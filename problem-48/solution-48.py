# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    first_list = []
    second_list = []
    for i in range(int(input("Input length for first list: "))):
        first_list.append(int(input()))
    for i in range(int(input("Input length for second list: "))):
        second_list.append(int(input()))
    temp = set(first_list + second_list)
    final_list = list(temp)
    print(sorted(final_list), "\n")
    x += 1
