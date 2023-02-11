import random
import string

# List of possible chars that can be used to generate random password
charList = string.ascii_letters + string.digits + string.punctuation

# List of all passwords the user accepts to keep
accepted_pw = []

# Method to generate password
def pw_gen():

  # User decides the length of the password string, not longer than 40 chars
  length = int(input("\nEnter length of password: "))
  if length < 40:

    # Temp list to hold all generated chars
    password = []
    for i in range(length):    

      # Pick a random char from char list
      randomchar = random.choice(charList)   

      # Add them to a temp list   
      password.append(randomchar)

    # Once picking process completes, combine the list of selected chars into a string
    final_pw = "".join(password)

    # Print out the generated password
    print("Password generated: "  + final_pw)

    # Ask if user wants to keep 
    opt = input("Accept? (Y/N) ")
    if opt.lower() == 'y':
      accepted_pw.append(final_pw) 
    else:
      pass 

  # Length of password should be less than 40 chars        
  else:
    print("ERROR! Length of password can't be more than 40 chars!")
  
  
# Print out the selection menu      
def print_menu():
  print("================================")
  print("1 - Start password generator")
  print("2 - Print accepted passwords")
  print("9 - Exit the program")
  opt = int(input("\nPlease select an option: "))
  while True: 
    if opt == 1 or opt == 2 or opt == 9:
      return opt
    else:
      print("***invalid option***")
      opt = input("Please enter a valid option: ")


# Program will continue to run until user decides when to quit
while True:

  # Print selection menu
  opt = print_menu()

  # Generate password
  if opt == 1:
    pw_gen()  

  # Print out password list  
  elif opt == 2:
    print("\nYour accepted passwords are:")
    for i in accepted_pw:
      print(i) 

  # Close the program
  else:
    print("\nThanks for using this program!")
    break
