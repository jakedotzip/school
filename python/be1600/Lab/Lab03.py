oldStr = input("Enter a string: ")

def swapChar(old):
  new = ""
  cs = 0
  for letter in old[1:-1]:
    if letter not in "aeiou ":
      new = new + "*"
      cs += 1
    else:
      new = new + letter     
  print("Old String: ", old.upper())
  print("New String: ", new.upper())
  print("Number of consonant characters:", cs)

swapChar(oldStr)
