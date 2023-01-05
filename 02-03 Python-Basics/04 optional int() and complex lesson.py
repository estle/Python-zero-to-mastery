# complex - another data type: for complex math, when faced, just google

print(bin(5))
print(int('0b101', 2))

# Python int() working w/ exceptions
try:
  print(int('0c101'))
except ValueError as e:
  print(e)
