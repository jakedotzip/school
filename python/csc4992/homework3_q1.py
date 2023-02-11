#make for loop
for i in range(147,62,-3):
  if i == 147:  #this will ignore the first number of the list
    count = 0
  else:
    print(i, end=" ")
    count+=1    #increase by 1 each time the program makes a loop
print("\nTotal time the program looped:", count)