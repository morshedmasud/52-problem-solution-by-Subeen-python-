# Taking value of 't' for test case
t = int(input())
x = 0
while x < t:
    # Taking value from user for 'sentence' and 'characters'
    sentence = input()
    characters = input()
    count = 0
    # Loop for checking every element to characters
    for i in sentence:
        if i == characters:
            count += 1
    if count:
        print("Occurrence of '%s' in '%s' = %d \n" %(characters, sentence, count))
    else:
        print("'%s' is not present \n" %characters)
    x += 1