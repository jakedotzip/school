import random
k = random.randint(1,10)

print("Enter", k, "values:")
numList = []
for i in range(k):
  num = int(input("Enter value " + str(i+1) + ": "))
  numList.append(num)
print("Original list: ", numList)

def is_sorted(l):
  if len(l) == 1:
    return True
  for i in l:
    if l[i] < l[i+1]:
      return True
    else:
      return False

if (is_sorted(numList) == True):
  print("The list is sorted")
else:
  print("The list is not sorted")