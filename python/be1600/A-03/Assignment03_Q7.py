my_file = open("tempconv.txt", "w")
f = []


my_file.write("{0:12s}{1:>s}\n".format("Fahrenheit","Celcius"))
for i in range(-10,11):
  f.append(i)

for i in range(0,len(f)):
  c = (f[i]-32)*5/9 
  my_file.write("{0:<12.2f}{1:0.2f}\n".format(f[i],c))
my_file.close()

my_file = open("tempconv.txt", "r")
print(my_file.read())
my_file.close()