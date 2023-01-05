sentence = input().split()
dictionary = {word:0 for word in sentence}
for word in sentence:
    dictionary[word] += 1
sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[0])
for key, value in sorted_dictionary:
    print(f'{key}:{value}')
