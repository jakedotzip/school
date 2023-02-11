my_file = open("numbers.txt", "r")

neg_count = 0
odd_count = 0
pos_sum = 0
neg_sum = 0
pos_avg = 0
count = 0

for line in my_file:
  l = line.split(" ")
  if (int(l[1]) < 0):
    neg_count += 1
  if ((int(l[1]))%2 == 1):
    odd_count += 1
  if (int(l[1]) < 0):
    neg_sum += int(l[1])
  if (int(l[1]) > 0):
    pos_sum += int(l[1])
    count += 1
    pos_avg = pos_sum/count
  
print("negative count =", neg_count)
print("odd count =", odd_count)
print("negative sum =", neg_sum)
print("positive average =", pos_avg)
