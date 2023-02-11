file = open("work.txt", "r")

separator = input("Choose separator: ") 
print()

for line in file:
  line = line.strip()
  x = line.split(':')
  print(x[0])

file.close()
print()