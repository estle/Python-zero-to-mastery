email = input()
username = email.split('@')[0]
print(username)

# import re

# email = "john@google.com elise@python.com"
# pattern = "(\w+)@\w+.com"
# ans = re.findall(pattern,email)
# print(ans)