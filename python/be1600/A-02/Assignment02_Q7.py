def vw_count(w): 
  vw = 0
  for letter in w:
    if letter in "aeiou":
      vw += 1
  return vw

def cs_count(c):
  cs = 0
  for letter in c:
    if letter not in "aeiou":
      cs += 1
  return cs

s = input("Enter a string: ")
print("The string you entered includes", vw_count(s), "vowels and", cs_count(s) ,"consonants")

