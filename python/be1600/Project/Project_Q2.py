dictionary = {}

# load information from a .txt file to dictionary
def load_info():
  my_file = open("data.txt","r")
  for line in my_file:
    line = line.strip()
    l = line.split(",")
    name = l[0]
    email = l[1]
    dictionary[name] = email
  my_file.close()

# save information in dictionary to a .txt file
def save_info():
  my_file = open("data.txt","w")
  for name, email in dictionary.items():
    my_file.write(str(name) + "," + str(email) + "\n")
  my_file.close()

# look up information
def lookup_info(name):
  load_info()   # using function to load info to the dictionary
  if name in dictionary.keys():
    return dictionary[name]

# add information to dictionary    
def add_info(name, email):
  dictionary[name] = email
  save_info()

# change information in the dictionary, then use save_info 
# function to update the .txt file
def change_info(name):
  email = input("Enter new email address: ")
  add_info(name, email)

# delete information from the dictionary, then use save_info
# function to update the .txt file
def delete_info(name):
  load_info()
  if name in dictionary.keys():
    dictionary[name] = None
    del dictionary[name]
    save_info()
    return True
  return False

# function to print menu
def print_menu():
  print("Menu")
  print("------------------------------")
  print("1. Look up an email address")   
  print("2. Add a new name and email address")
  print("3. Change an existing email address")
  print("4. Delete a name and email address")
  print("5. Quit the program")
  opt = input("\nEnter your choice: ")
  # this loop is to make sure only 1-5 are the accepted choices
  while True:
    if opt.isdigit():
      opt = int(opt)
      if opt == 1 or opt == 2 or opt == 3 or opt == 4 or opt == 5:
        return opt
      else:
        print("***invalid option***")
        opt = input("Please enter a valid option: ")
    else:
      print("***invalid option***")
      opt = input("Please enter a valid option: ")

# main function
def main():
  while True:
    opt = print_menu()
    if opt == 1:
      name = input("Enter name: ")
      email = lookup_info(name)
      if (email != None):
        print("Name: ", name)
        print("Email: ", email)
        print()
      else:
        print("The specified name was not found\n")

    elif opt == 2:
      name = input("Enter name: ")
      if (lookup_info(name) == True):
        print("Name already existed\n")
      else:
        email = input("Enter email address: ")
        add_info(name, email)
        print("Name and address have been added!\n")

    elif opt == 3:
      name = input("Enter name: ")
      email = lookup_info(name)
      if (email != None):
        change_info(name)
        print("Information updated!\n")
      else:
        print("The name is not in the database\n")
    
    elif opt == 4:
      name = input("Enter name: ")
      email = lookup_info(name)
      if (email != None):
        delete_info(name)
        print("Information deleted!\n")
      else:
        print("The name is not in the database\n")
        
    else:
      print("\nInformation saved!")
      break

main()

