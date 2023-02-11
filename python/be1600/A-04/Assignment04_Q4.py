import random
def three_heads():
  count = 0
  while (count != 3):
    n = random.randint(0,1)
    if (n == 0):
      print("H", end=' ')
      count += 1
    else:
      print("T", end=' ')
      count = 0

three_heads()
print("\nThree heads in a row!")