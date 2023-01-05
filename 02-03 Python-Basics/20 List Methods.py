basket = [1,2,3,4,5]

#adding
new_list = basket.append(100) # action that modifies by creating a new list, it returns None
print(basket)
print(new_list)

basket.insert(3, 330)
print(basket)

basket.extend([39, 4, 49])
print(basket)

#removing
basket.pop()
item = basket.pop(0) # removes the item at index and returns it
print(f'{item} was removed from the list {basket}')

basket.remove(4) # removes the value from the list
print(basket)

basket.clear() # empties the list completely
print(basket)
