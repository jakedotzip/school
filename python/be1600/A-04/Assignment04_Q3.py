def print_average():
  sum = 0
  count = 0
  n = int(input("Type a number: "))
  if n < 0:
    return 0
  else:
    while (n >= 0):
      count += 1
      sum += n
      n = int(input("Type a number: ")) 
    return sum/count
print("Average was", print_average())