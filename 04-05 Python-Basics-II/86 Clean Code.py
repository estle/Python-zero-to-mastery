# Clean Code - try to make it cleaner

# def is_even(num):
#   if num % 2 == 0:
#     return True
#   return False

# def is_even(num):
#   return True if num % 2 == 0 else False

# This is a Clean function that was built only from ~3 try

def is_even(num):
  return num % 2 == 0

print(is_even(50))
