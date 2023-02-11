import random

numList = []
odd = 0
even = 0

for i in range(100):
    numList.append(random.randint(1,1000))
    if (numList[i]%2 == 1):
        odd += 1
    else:
        even += 1

print ("Out of 100 random numbers, " + str(odd) + " were odd, and " + str(even) + " were even.")
