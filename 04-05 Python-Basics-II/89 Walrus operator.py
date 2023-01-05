# Walrus :=
a = 'ogbudday noy mayot'
if (n := len(a)) > 4:
  print(f'too long {n} elems')

while (n := a.count('a')) > 0:
  print(n)
  a = a.replace('a', 'X', 1)

print(a)

# Lesson look in 'What's New' section of python versions for possible coding simplifications 
