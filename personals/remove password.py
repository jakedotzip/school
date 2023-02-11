infile = open("personals\work.txt", "r")
outfile = open("personals\output.txt", "w")

while True:
  line = infile.readline().strip()
  if line == '':
    break
  else:
    x = line[:-17]
    outfile.write(x)
    outfile.write('\n')

infile.close()
outfile.close()
print("Done!~")