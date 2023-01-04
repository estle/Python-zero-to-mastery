# Scope - what variables do I have access to?
total = 100 # global scope

def some_func():
  func_var = 39 # local function var

# print(func_var)  not defined error

a = 1

def confusion():
  a = 10
  def child():
    return a
  return child()

print(confusion())
print(a)

# Scope Rules
#1 - start with local
#2 - Parent local?
#3 - Global
#4 - built in python functions
