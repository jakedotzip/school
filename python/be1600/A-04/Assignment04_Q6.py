import csv

my_file = open("earthquakes.csv","r")
rd = csv.reader(my_file)

micro, minor, light, moderate, major, strong, great = 0,0,0,0,0,0,0

next(my_file)
for line in rd:
  mag = float(line[4])
  if mag >= 0 and mag < 3:
    micro += 1
  if mag >= 3 and mag < 4:
    minor += 1
  if mag >= 4 and mag < 5:
    light += 1
  if mag >= 5 and mag < 6:
    moderate += 1
  if mag >= 6 and mag < 7:
    major += 1
  if mag >= 7 and mag < 8:
    strong += 1
  if mag >= 8:
    great += 1

print("{0:25s}{1:>s}".format("Criteria","Count"))
print("-"*30)
print("{0:25s}{1:>5n}".format("Micro(0 - 3)", micro))
print("{0:25s}{1:>5n}".format("Minor(3 - 3.9)", minor))
print("{0:25s}{1:>5n}".format("Light(4 - 4.9)", light))
print("{0:25s}{1:>5n}".format("Moderate(5 - 5.9)", moderate))
print("{0:25s}{1:>5n}".format("Major(6 - 6.9)", major))
print("{0:25s}{1:>5n}".format("Strong(7 - 7.9)", strong))
print("{0:25s}{1:>5n}".format("Great(>= 8)", great))