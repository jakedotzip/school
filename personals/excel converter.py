file = open("personals\work.txt", "r")

separator = input("Choose separator: ") 
print()

while True:
  line = file.readline().strip()
  if line == '':
    break
  else:
    x = line.replace("\t",separator)
    print(x)

file.close()
print()