# Enumerate - useful, when you need an index counter of iterable object
for i,char in enumerate('Hellloooo'):
  print(i,char)

for i,num in enumerate(list(range(100))):
  if num==50:
    print(i)
    break
print()
    
# While loops
i = 0
while i < 5:
  print(i)
  i += 1
  if i == -1:
    break # usage along with else is a really useful thing
else:
  print('no problems occured, sir')

# Pass
for item in [1,2,3]:
  pass # the place holder that just prevents error of an empty loop for example
