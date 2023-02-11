def encode():
  plain = str(input("Plain text: "))
  cipher = ""
  count = 0
  i = 2
  while count < len(plain):  
    jump = i
    while jump < len(plain):
      cipher += plain[jump]
      jump += 3
      count += 1
    i = i - 1
  return cipher
print(encode())