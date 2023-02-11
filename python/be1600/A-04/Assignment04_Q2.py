import random
def dice_sum():
  wanted = int(input("Desired dice sum: "))
  total = 0 
  while (total != wanted):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2
    print(dice1, "and", dice2, "=", total)
dice_sum()
  