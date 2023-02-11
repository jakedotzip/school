#############################################################################
#                                                                           #
#       Course:       CSC4992                                               #
#       Homework:     2                                                     #
#       Question:     2                                                     #
#       Name:         Huy Hoang                                             #
#                                                                           #
#############################################################################

gas_price = 3.49                                                    #variable to store gas price
gas_milage = float(input("Enter your gas milage on your car: "))    #ask user for MPG
distance = float(input("How far are you planning to travel? "))     #ask user for distance
cost = (distance/gas_milage)*gas_price                              #calculate the total cost
print("Total cost of your trip: $" + "{:.2f}".format(cost))         #display final result