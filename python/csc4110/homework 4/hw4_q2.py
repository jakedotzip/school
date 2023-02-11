import random
import time 

print("""
            GAME OF CHANCE
            """)

# List of all possible points to gain/loss
# Default value 0 means bankruptcy            
chances = [0]

# Method to roll for item in treasure chest
def choice(bank):

    # Select randomly from list that we generated with gen_point() method
    roll = random.choice(chances)

    # Value 0 means bankruptcy
    if roll == 0:
        print("BANKRUPT!!")
        bank = 0        
    else:

      # Gen a random number between 1 and 10
      # if a number is divided by 2, user gains point from the 'roll' variable above
      if random.randint(1,10) % 2 == 0:
        print("You received", roll)
        bank += roll

      # if not, balance will be deducted  
      else:
        print("You lost", roll)
        bank += roll
    return bank

# Method to generate all possible points
def gen_point():

  # Amount depends on user input
  items = int(input('Enter number of items in treasure chest: '))

  for i in range(items):

    # Minimum point will be 1000 and maximum point is 50000
    point = random.randint(1,50) * 100
    chances.append(point)

  # Print out list of all possible points  
  print("Item list = ", chances)
  print()

# Main method
def main():  

  # First we need to generate points
  gen_point() 

  # Initial balance a user has
  bank = 10000

  # Continue the game until balance reaches 0
  while bank >= 0: 
    
    # Roll for items
    bank = choice(bank)  

    # If we roll into 0, which means bankruptcy, the game stops
    if bank == 0:
      print("Game over!")
      break 
    else:  
      print("Current balance:", bank)
      print()

    # Sleep 2 seconds between each roll
    time.sleep(2)
    
main()