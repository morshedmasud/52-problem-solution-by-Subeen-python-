# showing all positive number between 1 to 1000
i = 1000
while i > 0:
    print(i, "\t", end='')
    i -= 1
    # when value of n % 5 == 0 is True then print a new line
    if i % 5 == 0:
        print()
