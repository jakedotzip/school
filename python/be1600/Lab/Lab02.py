import random

weight = random.randint(1,50)
priceList = [1.10, 2.20, 3.70, 4.50]
print("Package weight:", weight)

if (weight <= 2):
  print("Shipping rate: $" + str(priceList[1]))
  shipCharge = weight * priceList[1]
  print("Shipping charge: $" + str(shipCharge))
elif (2 < weight <= 6):
  print("Shipping rate: $" + str(priceList[2]))
  shipCharge = weight * priceList[2]
  print("Shipping charge: $" + str(shipCharge))
elif (6 < weight <= 10):
  print("Shipping rate: $" + str(priceList[3]))
  shipCharge = weight * priceList[3]
  print("Shipping charge: $" + str(shipCharge))
elif (10 < weight <= 20):
  print("Shipping rate: $" + str(priceList[4]))
  shipCharge = weight * priceList[4]
  print("Shipping charge: $" + str(shipCharge))
else:
  print("The package is over 20 pounds and cannot be shipped")