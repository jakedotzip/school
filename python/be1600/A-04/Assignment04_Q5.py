import csv
import statistics

my_file = open("iris.csv", "r")
rd = csv.reader(my_file)
setosa = []
virginica = []


next(my_file)
for line in rd:
  if "setosa" in line[4]:
    setosa.append(float(line[2]))
  elif "virginica" in line[4]:
    virginica.append(float(line[2]))


def correlation():
  xBar = statistics.mean(setosa)
  yBar = statistics.mean(virginica)
  xStd = statistics.stdev(setosa)
  yStd = statistics.stdev(virginica)
  num = 0.0
  for i in range(len(setosa)):
    num = num + (setosa[i] - xBar) * (virginica[i] - yBar)
  corr = num / ((len(setosa) - 1) * xStd * yStd)
  return corr


print("setosa petal length:", setosa)
print("virginica petal length:",virginica)
print("correlation between setosa and virginica petal length:", "{0:.2f}".format(correlation()))