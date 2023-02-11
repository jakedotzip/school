def getData():
  temperature = []
  highest = []
  lowest = []

  print("Enter highest temperatures for each month of the year.")
  for i in range(12):
    h = int(input("Month " + str(i+1) + ": "))
    highest.append(h)
  temperature.append(highest)

  print("Enter highest temperatures for each month of the year.")
  for i in range(12):
    l = int(input("Month " + str(i+1) + ": "))
    lowest.append(l)
  temperature.append(lowest)

  return temperature

def avgHigh(temperature):
  sum = 0
  for i in range(12):
    sum += temperature[0][i]
  avg = sum/12
  return avg

def avgLow(temperature):
  sum = 0
  for i in range(12):
    sum += temperature[1][i]
  avg = sum/12
  return avg

def highest(temperature):
  high = temperature[0][0]
  for i in range(12):
    if temperature[0][i] > high:
      high = temperature[0][i]
  return high

def lowest(temperature):
  low = temperature[1][0]
  for i in range(12):
    if temperature[1][i] > low:
      low = temperature[1][i]
  return low

def main():
  temperature = getData()
  print("List of the highest and lowest temperatures for each month of the year")
  for i in range(2):
    for j in range(12):
      print(temperature[i][j], end = ' ')
    print("")
  print("Average high temperature for the year ", avgHigh(temperature))
  print("Average low temperature for the year ", avgLow(temperature))
  print("Highest high temperature for the year ", highest(temperature))
  print("Lowest low temperature for the year ", lowest(temperature))

main()