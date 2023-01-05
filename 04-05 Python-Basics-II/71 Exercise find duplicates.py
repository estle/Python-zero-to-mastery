some_list = ['a','b','c','d','b','m','n','n']
found_dupl = []
for item in some_list:
  if some_list.count(item)>1 and item not in found_dupl:
    print(item)
    found_dupl += [item]
  