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
    ### ROUTINE A ###
    # for each characters in 'user' string
    for char in user:
      # if the character is not an alphabet
      if char.isalpha() == False:      
        #  replace that character with an empty string
        user = user.replace(char, "")
    # once finished checking all characters of a string, add the string to a storing string
    user_list += user + ", "
    # print out all entered users that were filtered
    print("current users: " + user_list)    
  # asking for new input
  user = input("\nenter your username: ")

