def remove_duplicates(old):
  new = []
  for i in old:
    if i not in new:
      new.append(i)
    else:
      pass
  return new

ogList =  ['be', 'be', 'is', 'not', 'or', 'question', 'that', 'the', 'to', 'to']
print(remove_duplicates(ogList))