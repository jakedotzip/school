def word_count(a):
  list = a.split()
  print("\'" + a + "\'", "->", len(list))

s = input("Enter a string: ")
word_count(s)