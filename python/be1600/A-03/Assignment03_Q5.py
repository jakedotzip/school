def histogram(x):
  list = []
  for i in x:
    if (i != ' '): 
      list.append(i)
  for i in "abcdefghijklmnopqrstuvwxyz":
    ctr = 0
    if i in x:
      ctr = x.count(i)
      print(i.upper(), "* " * ctr)

histogram(input("Enter a string: "))