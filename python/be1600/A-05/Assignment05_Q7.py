rows, cols = (4,3)
alpha = []

for i in range(rows):
  alpha.append([0]*cols)

print("Part a")
for i in range(rows):
  for j in range(cols):
    print(alpha[i][j], end = ' ')
  print("")

print("Part b")
for i in range(rows):
  if (i == 0):
    alpha[i] = [1]*cols
  else:
    alpha[i] = [3]*cols
  for j in range(cols):
    print(alpha[i][j], end = ' ')
  print("")

print("Part c")
for i in range(rows):
  alpha[i][0] = 2
  alpha[i][1] = alpha[i][0]*2
  alpha[i][2] = alpha[i][1]*2
for i in range(rows):
  for j in range(cols):
    print(alpha[i][j], end = ' ')
  print("")