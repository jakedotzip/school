# from tabulate import tabulate

# Create class
class Automobiles(object):
    def __init__(self, type, make, model, year, cost, efficiency, tanksize):
        if type == "Gas" or type == "Diesel" or type == "Electric":
          self.type = type
        else:
          print("invalid type of vehicle!")
        self.make = make
        self.model = model
        self.year = year
        self.cost = cost
        self.efficiency = efficiency
        self.tanksize = tanksize
    
    # Function to get trip cost for each vehicle
    def calc_trip_cost(self, distance):
        if self.type == "Gas":
          gas_used = distance/self.efficiency
          self.bill = 5.15 * gas_used
          return '${:.2f}'.format(self.bill)
        elif self.type == "Diesel":
          diesel_used = distance/self.efficiency
          self.bill = 4.39 * diesel_used
          return '${:.2f}'.format(self.bill)
        else:
          electric_used = distance/self.efficiency
          self.bill = 0.14 * electric_used
          return '${:.2f}'.format(self.bill)

    # Function to get total cost for each vehicle (trip cost + vehicle cost)
    def calc_total_cost(self):
        self.total = self.cost + self.bill
        return '${:,.2f}'.format(self.total)
    
    # Getters
    def getType(self):
        return self.type
    def getMake(self):
        return self.make
    def getModel(self):
        return self.model
    def getYear(self):
        return self.year
    def getCost(self):
        return '${:,}'.format(self.cost)
    def getEff(self):
        return self.efficiency
    def getSize(self):
        return self.tanksize

# Check if input is valid for vehicle type
def typeInput():
  type = input("Type (Gas/Diesel/Electric): ")
  while type:
    if type == "Gas" or type == "Diesel" or type == "Electric":
      return type
    else:
      print("***invalid option !***")
      type = input("Please re-enter vehicle type (Gas/Diesel/Electric): ")

# Create 3 objects 
car4 = Automobiles("Gas", "Ford", "F150", 2022, 29990, 20, 23)
car5 = Automobiles("Electric", "Tesla", "Model 3", 2022, 46990, 0.26, 50)
car6 = Automobiles("Diesel", "Chevrolet", "Cruze", 2019, 23144, 31, 13.5)

# Car 1
print("\nPlease enter car 1:")
car1 = Automobiles(typeInput(), 
                    input("Make: "), 
                    input("Model: "), 
                    int(input("Year: ")), 
                    int(input("Cost: ")), 
                    float(input("Efficiency (mpg or kWh): ")), 
                    float(input("Tank size (gals or kW): "))) 

# Car 2
print("\nPlease enter car 2:")                    
car2 = Automobiles(typeInput(), 
                    input("Make: "), 
                    input("Model: "), 
                    int(input("Year: ")), 
                    int(input("Cost: ")), 
                    float(input("Efficiency (mpg or kWh): ")), 
                    float(input("Tank size (gals or kW): "))) 

# Car 3
print("\nPlease enter car 3:")                    
car3 = Automobiles(typeInput(), 
                    input("Make: "), 
                    input("Model: "), 
                    int(input("Year: ")), 
                    int(input("Cost: ")), 
                    float(input("Efficiency (mpg or kWh/mile): ")), 
                    float(input("Tank size (gal or kWh): "))) 

# Get trip details from user input
city = input("\nWhere are you traveling to? ")
distance = float(input("What's the total distance (in miles) for a round trip to " + str(city) + " from Detroit? "))

# Sort all vehicles based on their costs
compare_list = [car1, car2, car3, car4, car5, car6]
sort_list = sorted(compare_list, key=lambda x: x.cost, reverse=True)

# Print out using "tabulate" library
header = ["Rank", "Type", "Make", "Model", "Year", "Efficiency", "Tank Size", "Vehicle Cost", "Trip Cost", "Total Cost"]
table = []
for i in range(len(sort_list)):
    car_details = []
    car_details.append(str(i+1))
    car_details.append(sort_list[i].getType())
    car_details.append(sort_list[i].getMake())
    car_details.append(sort_list[i].getModel())
    car_details.append(sort_list[i].getYear())
    car_details.append(sort_list[i].getEff()) 
    car_details.append(sort_list[i].getSize())
    car_details.append(sort_list[i].getCost())
    car_details.append(sort_list[i].calc_trip_cost(distance))
    car_details.append(sort_list[i].calc_total_cost())
    table.append(car_details)
print()
#print(tabulate(table, header))




# (optional) Print out using .format()

print()
print('{:8} {:12} {:12} {:15} {:<8} {:>12} {:>15} {:>15} {:>15} {:>15}'.format("Rank", "Type", "Make", "Model", "Year", "Efficiency", "Tank Size", "Vehicle Cost", "Trip Cost", "Total Cost"))
print('='*136)
for i in range(len(sort_list)):
    print('{:8} {:12} {:12} {:15} {:<8} {:>12} {:>15} {:>15} {:>15} {:>15}'.format(str(i+1),
                                                                        sort_list[i].getType(), 
                                                                        sort_list[i].getMake(),
                                                                        sort_list[i].getModel(),
                                                                        sort_list[i].getYear(), 
                                                                        sort_list[i].getEff(), 
                                                                        sort_list[i].getSize(),
                                                                        sort_list[i].getCost(),
                                                                        sort_list[i].calc_trip_cost(distance),
                                                                        sort_list[i].calc_total_cost()))

                                                                    









