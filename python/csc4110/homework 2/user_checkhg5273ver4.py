# ask user for input
user = list(input("enter your username: "))

# create a list to store all filtered users
user_list = []

# keep asking user until 'exit' is input
while True:
  if ''.join(user) == 'exit' :
    print("program stopped!")
    break
  else:    
    ### ROUTINE D ###

    # a string variable to store filtered username
    filtered_user = ""

    # loop thru 'user' list using while loop
    i = 0    
    while i < len(user):     
      # using list index, check if the element is an alphabet 
      if user[i].isalpha() == True:
        # add valid element to created string variable
        filtered_user += user[i]
      i += 1      
    # once finished checking all characters of a string, add the string to list of filtered user  
    user_list.append(filtered_user)
    # print out all entered users that were filtered
    print("current users: " + str(user_list))
  # asking for new input
  user = list(input("\nenter your username: "))

