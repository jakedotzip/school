import random

# root list
regions_list = ["East", "Central", "West", "South", "North"]
reps_list = ["Alexander", "Alfred", "Arthur", "Aaron", "Andrew", "Adam", "Andres", "Kelvin", "Henry", "Norton"]
items_dict = {"Sweatshirt":49.99, "Jean":99.99, "T-Shirt":29.99, "Hat":15.99, "Short":0.99, "Sneaker":79.99, "Socks":7.99}

# data list
date = []
region = []
rep = []
item = []
unit = []
total_cost = []

# generate data and append to data list
def genDate():  
  date.append(str(random.randint(1,12)) + "/" + str(random.randint(1,28)) + "/" + str(random.randint(2015,2022)))
def genRegion():
  region.append(random.choice(regions_list))
def genRep():
  rep.append(random.choice(reps_list))
def genUnit():
  unit.append(random.randint(1,100))
def genItems():  
  item.append(random.choice(list(items_dict)))
  total_cost.append(unit[-1]*items_dict[item[-1]])




# print out data lists in a nice format
print('{:15} {:15} {:15} {:15} {:<8} {:>12} {:>15}'.format("Order Date", "Region", "Rep", "Item", "Units", "Cost", "Total"))
print('='*101)
for i in range(10):
    genDate()
    genRegion()
    genRep()
    genUnit()
    genItems()
    print('{:15} {:15} {:15} {:15} {:<8} {:>12} {:>15.2f}'.format(date[i],
                                                                  region[i],
                                                                  rep[i],
                                                                  item[i],
                                                                  unit[i],
                                                                  items_dict[item[i]],
                                                                  total_cost[i]))