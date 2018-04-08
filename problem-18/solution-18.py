# Taking value of 't' from user for test case
t = int(input())
x = 0
while x < t:
    # creating vowels string and list's 'v' for store vowels and 'c' for consonent.
    vowel = 'aeiou'
    v = []
    c = []
    s = input()
    for j in range(len(s)):
        if s[j] in vowel:
            v.append(s[j])
        elif s[j] != ' ':
            c.append(s[j])
    print("".join(v))
    print("".join(c), "\n")
    x += 1