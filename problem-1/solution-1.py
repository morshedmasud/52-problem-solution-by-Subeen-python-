# Taking input from user for how many test we want
for_test = int(input("for test case: "))
# Running progamme basis user demanded test case
i = 0
while i < for_test:
    # Taking input a number from user for checking it's odd or evven
    n = int(input("Enter the number: "))
    # checking number is even or odd
    if n % 2 == 0:
        print('even', "\n")
    else:
        print('old', "\n")
    # Showing user have finished all test case
    if i == for_test-1:
        print('you have finished %d test case'% for_test)
    i += 1