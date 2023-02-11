import random
q_count = 0
c_count = 0

while(True): 
  print("Welcome to Math Practice")
  print("Enter 1 for Addition")
  print("Enter 9 to exit the test")
  num = int(input("pick an item from the menu: "))
  if(num == 1):
    a = random.randint(1,10)
    b = random.randint(1,10)
    print("what is", a, "+", b, "?", end=' ')
    ans = int(input())
    if (ans == a + b):
      print("Your answer is correct\n")
      q_count += 1
      c_count += 1
    else:
      print("Your answer is wrong\n")
      q_count += 1
  elif(num == 9):
    print("Number of questions:", q_count)
    print("Number of correct answers:", c_count)
    break
  else:
    print("Only accept 1 or 9 as input\n")