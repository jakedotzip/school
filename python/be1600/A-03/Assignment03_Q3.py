dict = {'a':15,'c':35,'b':10}

def printKeys():
  print("Keys: ", end="")
  for i in dict.keys():
    print(i, end=" ")

def printValues():
  print("\nValues: ", end="")
  for i in dict.values():
    print(i, end=" ")

def printPairs():
  print("\nKey-Value pairs")
  for k, v in dict.items():
    print(k, v)

def printKeysSorted():
  print("\nKey-Value pairs- sorted by key")
  for i in "abcdefghijklmnopqrstuvwxyz":
    if i in dict.keys():
      print(i, dict.get(i))

def printValuesSorted():
  print("\nKey-Value pairs- sorted by value") 
  n = dict.get('b') 
  print('b', dict.get('b'))
  for i in dict.keys():
    if (dict.get(i) > n):
      print(i, dict.get(i))
      n = dict.get(i)

printKeys()
printValues()
printPairs()
printKeysSorted()
printValuesSorted()