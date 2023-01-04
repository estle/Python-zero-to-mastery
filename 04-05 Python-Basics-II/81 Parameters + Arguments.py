# parameters - when we define the func
def sound(song='Godzilla', author='Eminem', rating='3.17'):
  print(f'i love {song} by {author}')

# arguments - when we call the func
sound('hello', 'adele', '2.43')
sound(author='pharrell williams', song='happy', rating='2.28')
sound() # goes with Default Parametres, those that were defined

# return
def _sum(num1, num2, num3):
  def _another_one(n3):
    return n3**2
  num1 + num2 + _another_one(num3)

def sum(num1, num2, num3):
  return num1 + num2 + num3

# Good Funtion should do one thing really well.
# It should return something.

print(_sum(3,9,5),sum(3,9,5))
