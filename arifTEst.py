"""
translation = {}
while True:
    word = input('Enter enlgish word: ')
    if word in translation:
        print(word, ' = ',translation[word])
    else:
        output = input('enter translation: ')
        translation[word] = output
"""

def cleanup(s):
    cleanline = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for character in s.lower():
        if character in alphabet:
            cleanline += character
        else:
            cleanline += ' '
    return cleanline

maxlength = 0
dicton = {}
with open('pap.txt') as book:
    for lines in book:
        for word in cleanup(lines).split():
            if word in dicton:
                dicton[word] += 1
            else:
                dicton[word] = 1
word = input('word? ')
print(dicton[word])

x = 100
while x > 0:
    print('fred')
    x -= 1


