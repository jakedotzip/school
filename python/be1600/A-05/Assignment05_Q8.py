year = int(input("Enter the number of year: "))

total = 0
for i in range(year):
  print("For year", i+1, ":")
  for j in range(12):
    n = float(input("Enter the rainfall amount for the month "+ str(j+1) +": "))
    total += n
avg = total/(year*12)

print("For", year*12, "months")
print("Total rainfall:", "{:.2f}".format(total), "inches")
print("Average monthly rainfall:", "{:.2f}".format(avg))