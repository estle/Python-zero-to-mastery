import re

s = "john@google.com me7@yandx.ru unity@x.com"
res = re.findall(r"\w+@(\w+).com", s)
print(*res, sep=', ')