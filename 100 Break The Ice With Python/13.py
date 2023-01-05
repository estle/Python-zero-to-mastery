sentence = input()
L = len([char for char in sentence if 'a'<=char<='z' or 'A'<=char<='Z'])
D = len([char for char in sentence if '0'<=char<='9'])
print(f'LETTERS {L} \nDIGITS: {D}')