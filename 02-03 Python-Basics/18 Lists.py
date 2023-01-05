li = [1,2,3,4,5]
li2 = ['a', 'b', 'c']
li3 = [1,2.3,'a',True]

# Data Structure, good way of storing the list
amazon_cart = [
  'notebook',
  'sunglasses',
  'laptop',
  'iphone',
  'grapes'
]
print(amazon_cart[-1])

# List slicing
print(amazon_cart[1::2])
amazon_cart[0] = 'daily planner'
print(amazon_cart[1:3], end='\nCompare:\n')
# Imprtant concept of pointing to the list, we copy by [:]
new_cart = amazon_cart
new_cart[0] = 'stranger things series'
print(new_cart)
print(amazon_cart, end='\nand\n')
# look at this, we use [:] instead
amazon_cart[0] = 'wow'
new_cart = amazon_cart[:]
new_cart[0] = 'no more stranger things'
print(new_cart)
print(amazon_cart)
