import random

name = input("Enter the name of the file to which results should be written: ")
num = int(input("Enter the number of random numbers to be written to the file: "))

my_file = open(name, "w")
for i in range(num):
  my_file.write(str(random.randint(1,100)))
  my_file.write("\n")
my_file.close()

my_file = open(name, "r")
print(my_file.read())
my_file.close()
