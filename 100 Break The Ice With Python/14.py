sentence = input()
print(f'UPPER CASE {sum(1 for char in sentence if char.isupper())}\
    \nLOWER CASE {sum(1 for char in sentence if char.islower())}')