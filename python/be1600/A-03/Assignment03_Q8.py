oldFile = open("thisFile.txt", "r")
newFile = open("thatFile.txt", "w")

i = 0
for line in oldFile:
  if i%2 == 0:
    newFile.write(line)
  i = i+1

oldFile.close()
newFile.close()

newFile = open("thatFile.txt", "r")
print(newFile.read())
newFile.close()
