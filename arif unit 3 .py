##    passwords = {'smith':'apple', 'jones':'a34xx', 'brown':'zzzz'}
##    username = input('username: ')
##    password = input('Password: ')
##    if password == passwords[username]:
##        print('You are logged in.')
##    else:
##       print('Bad password.')

##2
"""
concordance = {}
with open('pap1.txt') as book:
    linenum = 1
    for line in book:
        for word in line.split():
            if word in concordance:
                concordance[word].append(linenum)
            else:
                concordance[word] = [linenum]
        linenum += 1
print('Test:', concordance['property'])

concordance = {}
with open('pap1.txt') as book:
    linenum = 1
    for line in book:
        for word in line.split():
            if word in concordance:
                concordance[word].append(linenum)
            else:
                concordance[word]=[linenum]
        linenum += 1
while True:
    word = input('Enter word: ')
    if word in concordance:
        print('Found on lines:', concordance[word])
    else:
        print('Not found.')

##4
concordance = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'
with open('pap1.txt') as book:
    linenum = 1
    for line in book:
        cleanline = ''
        for character in line.lower():
            if character in alphabet:
                cleanline += character
            else:
                cleanline += ' '
        for word in cleanline.split():
            if word in concordance:
                concordance[word].append(linenum)
            else:
                concordance[word]=[linenum]
        linenum += 1
while True:
    word = input('Enter word: ')
    if word in concordance:
        print('Found on lines:', concordance[word])
    else:
        print('Not found.')
"""
def cleanedup(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cleantext = ''
    for character in s.lower():
        if character in alphabet:
            cleantext += character
        else:
            cleantext += ' '
    return cleantext
concordance = {}
with open('pap1.txt') as book:
    linenum = 1
    for line in book:
        for word in cleanedup(line).split():
            if word in concordance:
                concordance[word].append(linenum)
            else:
                concordance[word]=[linenum]
        linenum += 1
while True:
    word = input('Enter word: ')
    if word in concordance:
        print('Found on lines:', concordance[word])
    else:
        print('Not found.')


