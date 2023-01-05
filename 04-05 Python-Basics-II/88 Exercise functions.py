def highest_even(li):
  answer = None
  for item in sorted(li):
    if item % 2 == 0:
      answer = item
  return answer

print(highest_even([10,2,3,4,8,14,11]))
