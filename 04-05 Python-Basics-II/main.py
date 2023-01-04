# global + nonlocal Keywords
total = 0

# def count():
#   # total += 1 error
#   global total
#   total += 1
#   return total

def count(total):
  x = 7
  def inner():
    nonlocal x # x = 7
    x = 9 # changes value from 7 to 9
  total += 1
  return total

print(count(count(count(total))))
