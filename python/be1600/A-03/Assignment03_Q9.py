import string

name = input("Enter file name: ")
my_file = open(name, "r")
print("letter count")
dict= {}

#store letters to dictionary with value of 0
for i in string.ascii_lowercase:
  dict[i] = 0

for line in my_file:  #read all lines from input files
  line = line.lower()   #set all characters to lowercase
  for letter in line:   #read all characters in each line
    if letter in dict.keys():   #counts the frequency
      dict[letter] += 1  
    else: #ignore punctuations and digits
      pass

#read from the dictionary
for k in dict.keys(): 
    print(k, dict.get(k))
