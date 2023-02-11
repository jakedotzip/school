my_file = open("books.txt" , "r")

dict = {}

for line in my_file:
  line = line.strip()
  l = line.split(", ")
  for i in line:
    author = l[1].split(" ")
    last_name = author[-1]
    book = l[0].strip()
  if last_name not in dict:
    dict[last_name] = [book]
  else:
    dict[last_name].append(book)
      
for k in dict.keys(): 
  print(k, dict.get(k)) 