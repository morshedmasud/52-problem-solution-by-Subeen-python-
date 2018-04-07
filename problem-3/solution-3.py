# showing all positive number between 1 to 1000
# Counter for new line
counter = 0
i = 1000
while i > 0:
    counter +=1
    # when value of counter % 5 == 0 is True then print a new line
    if counter%5 == 0:
        print(i, "\t", end='\n')
    else:
        print(i, "\t", end='')
    i -= 1

