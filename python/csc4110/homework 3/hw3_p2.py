list1 = [78,56,8,12,90,21,71,98,101,1245,1600]
list2 = []

for i in range(len(list1)):
    if i == 0:
        list2.append(list1[0] + list1[1])
    elif 0 <i<len(list1)-1:
        list2.append(list1[i-1] + list1[i+1])
    elif i == len(list1) -1:
        list2.append(list1[len(list1)-1] + list1[len(list1)-2])
    
print("Old list: ", list1)
print("New list: ", list2)