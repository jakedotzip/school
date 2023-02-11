import math

def calc_dist(p1, p2):
  sum = 0
  for i in range(len(p1)):
    diff = (p1[i] - p2[i]) ** 2
    sum += diff
  distance = math.sqrt(sum)
  return distance

def main():
  my_file = open("data.txt", "r")
  lines = my_file.readlines()
  list = []
  for l in lines:
    list.append(l.strip().split(" "))

  # print table header
  for i in range(len(list)):
    print("{0:>7}{1:>1}".format("P", i+1), end = '')
  print()

  for i in range(len(list)):
    print("{0:1}{1:<1}".format("P", i+1), end = '')
    for j in range(i+1, len(list)):
      print("A")

main()