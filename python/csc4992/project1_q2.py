# Request name
name = input("Enter your first and last name: ")

# Request type of service
print("What type of service you want to subscribe?")
print("1 - Basic ($50)")
print("2 - Premium ($90)")
opt = int(input("Choose an option: "))
while True:
  if opt == 1:
    service_type = "Basic"
    service_price = 50
    tax = 6.50
    extra_channel = 0
    extra_fees = 0
    break
  elif opt == 2:
    service_type = "Premium"
    service_price = 90
    tax = 9.25
    extra_channel = int(input("How many pay per view channels would you like to add on ($9.99 per channel)? "))
    extra_fees = extra_channel*9.99
    break
  else:
    print("***invalid option !***")
    opt = int(input("Please enter a valid option (1 or 2): "))
    

# Request past balance
yes_no = input("Have you paid last month balance (Y/N)? ")
ch = yes_no.lower()
while True:
  if ch == 'n':
    balance = int(input("What is your current balance? "))
    late_fees = balance*0.1
    break
  elif ch == 'y':
    balance = 0
    late_fees = 0
    break
  else:
    print("***invalid option !***")
    opt = input("Please enter a valid option (Y or N): ")
    

# Output
total = service_price + tax + extra_fees + balance + late_fees
print("-"*40)
print("{0:^40s}".format("Python TV"))
print("{0:<25s}{1:>10s}".format("Customer Name:", name))
print("{0:<25s}{1:>10s}".format("Service Type:", service_type))
print("{0:<25s}{1:>10d}".format("Extra channels:", extra_channel))
print("-"*40)
print("{0:<25s}{1:>10.2f}".format("Base Price:", service_price))
print("{0:<25s}{1:>10.2f}".format("Tax:", tax))
print("{0:<25s}{1:>10.2f}".format("Extra channels fees:", extra_fees))
print("{0:<25s}{1:>10.2f}".format("Existing balance:", balance))
print("{0:<25s}{1:>10.2f}".format("Late fees:", late_fees))
print("-"*40)
print("{0:<25}{1:>10.2f}".format("Total:", total))
print("\nThank you for using Python TV services :)")