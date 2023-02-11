numList = []
for i in range(10):
  numList.append(int(input("Enter a number: ")))

max = numList[0]
for i in range (1, len(numList)):
  if numList[i] > max:
    max = numList[i]

min = numList[0]
for i in range (1, len(numList)):
  if numList[i] < min:
    min = numList[i]

sum = numList[0]
for i in range (1, len(numList)):
    sum += numList[i]

avg = sum/len(numList)

print("Low:", min)
print("High:", max)
print("Total:", sum)
print("Average:", avg)