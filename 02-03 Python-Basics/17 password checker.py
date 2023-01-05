username = input('username: ')
password = input('password: ') 
pass_len = len(password)
if pass_len>2: 
  hidden_password = password[0] + (pass_len-1)*'*'
else:
  hidden_password = pass_len*'*'

print(f'{username}, your  password [{hidden_password}] is {pass_len} letters long')
