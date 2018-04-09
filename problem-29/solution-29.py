# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    n = input()
    if n >= 'A' and n < 'Z':
        print('Uppercase character \n')
    elif n >= 'a' and n < 'z':
        print('Lowercase character \n')
    elif n >= '1' and n < '9':
        print("Numerical Digit \n")
    else:
        print("Special character \n")
    x += 1