# ask user for input
user = input("enter your username: ")

# create a string variable to store all entered users
user_list = ""

# keep asking user until 'exit' is input
while True:
  if user == 'exit':
    print("program stopped!")
    break
  else:    
    ### ROUTINE B ###
    # using filter() method to check each character in user string
    # then filter them out and combine all valid characters into a new string variable
    new_user = ''.join(filter(str.isalpha, user))
    # once finished checking all characters of a string, add the string to a storing string
    user_list += user + ", "
    # print out all entered users that were filtered
    print("current users: " + user_list)    
  # asking for new input
  user = input("\nenter your username: ")

