tixA = 15
tixB = 12
tixC = 9
seatNumA = int(input("Enter number of A seats: "))
seatNumB = int(input("Enter number of B seats: "))
seatNumC = int(input("Enter number of C seats: "))

incomeA = seatNumA * tixA
incomeB = seatNumB * tixB
incomeC = seatNumC * tixC

print("Income from class A seats: $ " + str(incomeA))
print("Income from class B seats: $ " + str(incomeB))
print("Income from class C seats: $ " + str(incomeC))

print("Total income: $ " + str(incomeA + incomeB + incomeC))