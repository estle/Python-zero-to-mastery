# Ternary Operator
is_friend = 1
can_message = 'message allowed' if is_friend else 'not allowed'
print(can_message)

# Short Circuiting
is_friend = 0
if True or is_friend:
  print('didn\'t check is_friend')

# Logical Operators
print( 1 < 2 > 3 < 4 ) # < > == >= <= != and or not

# Exercise on Logic, Focus on Readability to become a good dev
is_magician = False
is_expert = True
# check if magician AND expert: "you're a master magician"
# check if magician but not expert: "at least you're getting there"
# if you're not a magician: "Y0u need magic powers"
if is_magician and is_expert:
  print("you're a master magician")
elif is_magician and not is_expert:
  print("at least you're getting there")
elif not is_magician:
  print("Y0u need magic powers")

# is vs ==
print('1' == 1)
print([1,2,3] is [1,2,3]) # checks if they point to the same memory space
print('1' is '1') # is doesnt work with data structures
