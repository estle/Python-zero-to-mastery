birth_date = input('what is your birthday date? [dd:mm:yy]')
birth_day = int(birth_date[:2])
birth_month = int(birth_date[3:5])
birth_year = int(birth_date[-4:])

# get today
from datetime import date

today = date.today()

# dd/mm/YY
day = int(today.strftime("%d"))
month = int(today.strftime("%m"))
year = int(today.strftime("%Y"))
# print(f'{day}/{month}/{year}')

# this year birthday has passed
if month>birth_month or month==birth_month and day>=birth_day:
  print(f'Your age is {2022-birth_year}')
else:
  print(f'Your age is {2021-birth_year}')
