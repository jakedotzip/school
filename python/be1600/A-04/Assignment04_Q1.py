sum = 0
while True:  
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter another number: "))
  sum = num1 + num2
  print("The sum of the numbers you entered is", float(sum))
  repeat = input("Do you want to do that again? (y/n): ")
  if repeat == "n":
    break