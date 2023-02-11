# Create a list
WSU_List = [7,9,'a','cat',False]

# Append 3.14 and 7 to created list
WSU_List.append(3.14)
WSU_List.append(7)

# Insert 'dog' in position 3
WSU_List.insert(3, 'dog')

# Find the index of 'cat'
print("Index of 'cat': " + str(WSU_List.index('cat')))

# Count how many 7s in list
print("Number of 7s: " + str(WSU_List.count(7)))

# Remove the first 7 from list
WSU_List.remove(7)

# Remove 'dog' from list using pop() method
WSU_List.pop(WSU_List.index('dog'))
print(WSU_List)