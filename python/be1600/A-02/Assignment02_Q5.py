s = input("Enter a string: ")
num = int(input("Enter a number: "))

def repl(a, i):
  acc = a * i
  print(a, "->", acc)
repl(s, num)