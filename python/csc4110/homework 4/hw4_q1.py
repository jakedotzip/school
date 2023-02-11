import random
import string

data_dict = {}

def gen_username():
  char_holder = []
  for i in range(12):
    char = random.choice(string.ascii_lowercase)
    char_holder.append(char)
  for i in range(2):
    digit = random.choice(string.digits)
    char_holder.append(digit)
  username = ''.join(char_holder)
  return username

def gen_password():
  char_holder = []
  for i in range(16):
    char = random.choice(string.ascii_letters + string.digits)
    char_holder.append(char)
  password = ''.join(char_holder)
  return password

def gen_birthday():
  month = random.randint(1,12)
  day = random.randint(1,28)
  year = random.randrange(1950,2005)
  birthday = ''.join(str(month) + '/' + str(day) + '/' + str(year))
  return birthday

def gen_ssn():
  char_holder = []
  for i in range(10):
    if i == 3 or i == 6:
      char_holder.append('-')
    else:
      char_holder.append(random.choice(string.digits))
  ssn = ''.join(char_holder)
  return ssn

print(gen_ssn())

