file1 = open("file1.txt","r")
file2 = open("file2.txt","r")
output = open("output.txt","w")

list1 = []
list2 = []
for line in file1:
  for word in line.split():
    list1.append(word)
for line in file2:
  for word in line.split():
    list2.append(word)

uniqueList1 = []
output.write("Unique words contained in file 1:\n")
for i in list1:
  if i not in uniqueList1:
    uniqueList1.append(i)
for w in uniqueList1:    
  output.write(w + "\n")

uniqueList2 = []
output.write("\nUnique words contained in file 2:\n")
for i in list2:
  if i not in uniqueList2:
    uniqueList2.append(i)
for w in uniqueList2:    
  output.write(w + "\n")

both = []
output.write("\nWords that appeared in both files:\n")
for i in uniqueList1:
  for j in uniqueList2:
    if i == j:
      both.append(j)
for w in both:    
  output.write(w + "\n")

first = []
output.write("\nWords that appeared in file 1 only:\n")
for i in uniqueList1:
  if i not in uniqueList2:
    first.append(i)
for w in first:    
  output.write(w + "\n")

second = []
output.write("\nWords that appeared in file 2 only:\n")
for i in uniqueList2:
  if i not in uniqueList1:
    second.append(i)
for w in second:    
  output.write(w + "\n")

either = []
output.write("\nWords that appeared in either files but not both:\n")
for i in first:
  either.append(i)
for j in second:
  either.append(j)
for w in either:    
  output.write(w + "\n")