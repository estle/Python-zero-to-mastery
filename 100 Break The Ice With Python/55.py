import re

s = "234 c2ats and 33483 5dogs. 90"
ans = re.findall(r"\b\d+\b", s)
print(ans)