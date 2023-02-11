file = open("personals\work.txt", "r")
arr = []
line = file.readline()
  
while True:
  line = file.readline().strip()
  if line == '':
    break
  else:
    arr.append(line)

for i in range(len(arr)):
  print(arr[i] + ',', end='')