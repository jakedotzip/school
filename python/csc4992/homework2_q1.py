########################################################
#                                                      #
#       Course:       CSC4992                          #
#       Homework:     2                                #
#       Question:     1                                #
#       Name:         Huy Hoang                        #
#                                                      #
########################################################

# Request input from user
fname = input("Please enter your first name: ")
work_hours = int(input("How many hours did you work per week? "))
pay_rate = float(input("How much did you get paid per hour? $"))
overtime_hours = int(input("How many hours did you work overtime? "))

# Calculate
wage = work_hours * pay_rate
extra = overtime_hours * pay_rate * 1.5
gross_pay = wage + extra

# Tax rate variables
fica = 0.062 * gross_pay
medicare = 0.0145 * gross_pay 
state_tax = 0.0425 * gross_pay
fed_tax = 0.24 * gross_pay
city_tax = 0.009 * gross_pay
park_tax = 0.006 * gross_pay
home_pay = gross_pay - fica - medicare - state_tax - fed_tax - city_tax - park_tax

# Print out final results
print("="*50)
print("\nName:", fname)
print("Gross pay: $" + "{:.2f}".format(gross_pay))
print("\nFICA: -$" + "{:.2f}".format(fica))
print("Medicare: -$" + "{:.2f}".format(medicare))
print("State Tax: -$" + "{:.2f}".format(state_tax))
print("Federal Tax: -$" + "{:.2f}".format(fed_tax))
print("City Tax: -$" + "{:.2f}".format(city_tax))
print("Park Tax: -$" + "{:.2f}".format(park_tax))
print("\nHome Pay: $" + "{:.2f}".format(home_pay))

