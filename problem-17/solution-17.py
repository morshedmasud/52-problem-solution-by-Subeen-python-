# Taking value of 't' from user for test case
t = int(input())
x = 0
vowels = 'aeiou'
while x < t:
    # Taking input from user for 'sentence'.
    sentence = input()
    count = 0
    # loop in every characters in sentene
    for i in sentence:
        # checking i if is it member of vowels.
        if i in vowels:
            count += 1
    print("Number of vowels = %d \n" %count)
    x += 1
