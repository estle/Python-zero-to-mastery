basket = ['a','b','c','d','ee']

try:
  print(basket.index('d', 0, 3))
except:
  print('d' in basket)
print('f' in basket)
print('i' in 'hi my name is Ivan')

print(basket.count('e'))

# using this list, 
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list
basket.remove('Banana')
# 2. Remove "Blueberries" from the list.
basket.pop()
# 3. Put "Kiwi" at the end of the list.
basket.append('Kiwi')
# 4. Add "Apples" at the beginning of the list
basket.insert(0, 'Apples')
# 5. Count how many apples in the basket
basket.count('Apples')
# 6. empty the basket
basket.clear()
print(basket)
