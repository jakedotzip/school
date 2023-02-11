# Getting names and store in a llist
USA_names = []
CAN_names = []
IND_names = []
all_names = []
print("\n\n")
print("*"*100)
print("*" + " "*98 + "*")
print("*", "{0:>50}".format("NAME REGISTER"), "{0:>47}".format("*"))
print("*" + " "*98 + "*")
print("*"*100)
for i in range(5):
  name = input("Enter USA bowler #" + str(i+1) + " name: ")
  USA_names.append(name)
  all_names.append(name)
print()
for i in range(5):
  name = input("Enter Canada bowler #" + str(i+1) + " name: ")
  CAN_names.append(name)
  all_names.append(name)
print()
for i in range(5):
  name = input("Enter India bowler #" + str(i+1) + " name: ")
  IND_names.append(name)
  all_names.append(name)

###### ROUND 1 #######
USA_score1 = []
CAN_score1 = []
IND_score1 = []

print("\n###### ROUND 1 #######\n")
print("------- Team USA -------")
for i in range(5):
  score = int(input("Enter " + str(USA_names[i]) + "'s score: "))
  while(score<0 or score>300):
    print("Invalid input! Please enter number between 0 and 300")
    score = int(input("Enter " + str(USA_names[i]) + "'s score: "))
  else:
    USA_score1.append(score)

print("------- Team Canada -------")
for i in range(5):
  score = int(input("Enter " + str(CAN_names[i]) + "'s score: "))
  while(score<0 or score>300):
    print("Invalid input! Please enter number between 0 and 300")
    score = int(input("Enter " + str(CAN_names[i]) + "'s score: "))
  else:
    CAN_score1.append(score)

print("------- Team India -------")
for i in range(5):
  score = int(input("Enter " + str(IND_names[i]) + "'s score: "))
  while(score<0 or score>300):
    print("Invalid input! Please enter number between 0 and 300")
    score = int(input("Enter " + str(IND_names[i]) + "'s score: "))
  else:
    IND_score1.append(score)

total_USA_score1 = sum(USA_score1)
total_CAN_score1 = sum(CAN_score1)
total_IND_score1 = sum(IND_score1)

###### ROUND 2 #######
USA_score2 = []
CAN_score2 = []
IND_score2 = []

print("\n\n###### ROUND 2 #######\n")
print("------- Team USA -------")
for i in range(5):
  score = int(input("Enter " + str(USA_names[i]) + "'s score: "))
  while(score<0 or score>300):
    print("Invalid input! Please enter number between 0 and 300")
    score = int(input("Enter " + str(USA_names[i]) + "'s score: "))
  else:
    USA_score2.append(score)

print("------- Team Canada -------")
for i in range(5):
  score = int(input("Enter " + str(CAN_names[i]) + "'s score: "))
  while(score<0 or score>300):
    print("Invalid input! Please enter number between 0 and 300")
    score = int(input("Enter " + str(CAN_names[i]) + "'s score: "))
  else:
    CAN_score2.append(score)

print("------- Team India -------")
for i in range(5):
  score = int(input("Enter " + str(IND_names[i]) + "'s score: "))
  while(score<0 or score>300):
    print("Invalid input! Please enter number between 0 and 300")
    score = int(input("Enter " + str(IND_names[i]) + "'s score: "))
  else:
    IND_score2.append(score)

total_USA_score2 = sum(USA_score2)
total_CAN_score2 = sum(CAN_score2)
total_IND_score2 = sum(IND_score2)


###### ROUND 3 #######
USA_score3 = []
CAN_score3 = []
IND_score3 = []

print("\n###### ROUND 3 #######\n")
print("------- Team USA -------")
for i in range(5):
  score = int(input("Enter " + str(USA_names[i]) + "'s score: "))
  while(score<0 or score>300):
    print("Invalid input! Please enter number between 0 and 300")
    score = int(input("Enter " + str(USA_names[i]) + "'s score: "))
  else:
    USA_score3.append(score)

print("------- Team Canada -------")
for i in range(5):
  score = int(input("Enter " + str(CAN_names[i]) + "'s score: "))
  while(score<0 or score>300):
    print("Invalid input! Please enter number between 0 and 300")
    score = int(input("Enter " + str(CAN_names[i]) + "'s score: "))
  else:
    CAN_score3.append(score)

print("------- Team India -------")
for i in range(5):
  score = int(input("Enter " + str(IND_names[i]) + "'s score: "))
  while(score<0 or score>300):
    print("Invalid input! Please enter number between 0 and 300")
    score = int(input("Enter " + str(IND_names[i]) + "'s score: "))
  else:
    IND_score3.append(score)

total_USA_score3 = sum(USA_score3)
total_CAN_score3 = sum(CAN_score3)
total_IND_score3 = sum(IND_score3)



########### CALCULATION ###########
final_USA_score = total_USA_score1 + total_USA_score2 + total_USA_score3
final_CAN_score = total_CAN_score1 + total_CAN_score2 + total_CAN_score3
final_IND_score = total_IND_score1 + total_IND_score2 + total_IND_score3

avg_USA_score = final_USA_score/15
avg_CAN_score = final_CAN_score/15
avg_IND_score = final_IND_score/15

individual_avg = []
for i in range(5):
  a = (USA_score1[i] + USA_score2[i] + USA_score3[i])/3
  individual_avg.append(a)
for i in range(5):
  a = (CAN_score1[i] + CAN_score2[i] + CAN_score3[i])/3
  individual_avg.append(a)
for i in range(5):
  a = (IND_score1[i] + IND_score2[i] + IND_score3[i])/3
  individual_avg.append(a)



######### SCOREBOARD ##########
print("\n\n")
print("*"*100)
print("*" + " "*98 + "*")
print("*", "{0:>50}".format("SCOREBOARD"), "{0:>47}".format("*"))
print("*" + " "*98 + "*")
print("*"*100)


print("\n", " "*45, "TEAM USA")
print("{0:<20}".format("Bowler"), "Round 1\t\tRound 2\t\tRound3\t\tAverage Score")
for i in range(5):
  print("{0:<20}".format(USA_names[i]), USA_score1[i], "\t\t", USA_score2[i], "\t\t", USA_score3[i], "\t\t", "{0:.2f}".format(individual_avg[i]))
print("-"*100)
print("{0:<20}".format("Total"), total_USA_score1, "\t\t", total_USA_score2, "\t\t", total_USA_score3, "\t\t", "{0:.2f}".format(avg_USA_score))
print("="*100)

print("\n", " "*45, "TEAM CANADA")
print("{0:<20}".format("Bowler"), "Round 1\t\tRound 2\t\tRound3\t\tAverage Score")
for i in range(5):
  print("{0:<20}".format(CAN_names[i]), CAN_score1[i], "\t\t", CAN_score2[i], "\t\t", CAN_score3[i], "\t\t", "{0:.2f}".format(individual_avg[5+i]))
print("-"*100)
print("{0:<20}".format("Total"), total_CAN_score1, "\t\t", total_CAN_score2, "\t\t", total_CAN_score3, "\t\t", "{0:.2f}".format(avg_CAN_score))
print("="*100)

print("\n", " "*45, "TEAM INDIA")
print("{0:<20}".format("Bowler"), "Round 1\t\tRound 2\t\tRound3\t\tAverage Score")
for i in range(5):
  print("{0:<20}".format(IND_names[i]), IND_score1[i], "\t\t", IND_score2[i], "\t\t", IND_score3[i], "\t\t", "{0:.2f}".format(individual_avg[10+i]))
print("-"*100)
print("{0:<20}".format("Total"), total_IND_score1, "\t\t", total_IND_score2, "\t\t", total_IND_score3, "\t\t", "{0:.2f}".format(avg_IND_score))
print("="*100)

######### FINAL RESULT ###########

print("\n\n")
print("*"*100)
print("*" + " "*98 + "*")
print("*", "{0:>50}".format("FINAL RESULT"), "{0:>47}".format("*"))
print("*" + " "*98 + "*")
print("*"*100)

## Round 1 winner
if (total_USA_score1 == max(total_CAN_score1,total_IND_score1,total_USA_score1)):
  print("The winner in round 1 is: TEAM USA")
elif (total_CAN_score1 == max(total_CAN_score1,total_IND_score1,total_USA_score1)):
  print("The winner in round 1 is: TEAM CANADA")
elif (total_IND_score1 == max(total_CAN_score1,total_IND_score1,total_USA_score1)):
  print("The winner in round 1 is: TEAM INDIA")

## Round 2 winner
if (total_USA_score2 == max(total_CAN_score2,total_IND_score2,total_USA_score2)):
  print("The winner in round 2 is: TEAM USA")
elif (total_CAN_score2 == max(total_CAN_score2,total_IND_score2,total_USA_score2)):
  print("The winner in round 2 is: TEAM CANADA")
elif (total_IND_score2 == max(total_CAN_score2,total_IND_score2,total_USA_score2)):
  print("The winner in round 2 is: TEAM INDIA")

## Round 3 winner
if (total_USA_score3 == max(total_CAN_score3,total_IND_score3,total_USA_score3)):
  print("The winner in round 3 is: TEAM USA")
elif (total_CAN_score3 == max(total_CAN_score3,total_IND_score3,total_USA_score3)):
  print("The winner in round 3 is: TEAM CANADA")
elif (total_IND_score3 == max(total_CAN_score3,total_IND_score3,total_USA_score3)):
  print("The winner in round 3 is: TEAM INDIA")

## Overall winner
if (final_USA_score == max(final_USA_score,final_CAN_score,final_IND_score)):
  print("\nThe best bowling team is : TEAM USA")
elif (final_CAN_score == max(final_USA_score,final_CAN_score,final_IND_score)):
  print("\nThe best bowling team is : TEAM CANADA")
elif (final_IND_score == max(final_USA_score,final_CAN_score,final_IND_score)):
  print("\nThe best bowling team is : TEAM INDIA")

## Individual prize
gold_score = individual_avg[0]
gold_name = all_names[0]
for i in range (1, len(individual_avg)):
  if individual_avg[i] > gold_score:
    gold_score = individual_avg[i]
    gold_name = all_names[i]
individual_avg.remove(gold_score)
all_names.remove(gold_name)

silver_score = individual_avg[0]
silver_name = all_names[0]
for i in range (1, len(individual_avg)):
  if individual_avg[i] > silver_score:
    silver_score = individual_avg[i]
    silver_name = all_names[i]
individual_avg.remove(silver_score)
all_names.remove(silver_name)

bronze_score = individual_avg[0]
bronze_name = all_names[0]
for i in range (1, len(individual_avg)):
  if individual_avg[i] > bronze_score:
    bronze_score = individual_avg[i]
    bronze_name = all_names[i]
individual_avg.remove(bronze_score)
all_names.remove(bronze_name)

print()
print("{0:<10}".format("Medal"), "{0:<30}".format("Name"), "{0:>20}".format("Score"))
print("-"*65)
print("{0:<10}".format("Gold"), "{0:>30}".format(gold_name), "{0:>20.2f}".format(gold_score))
print("{0:<10}".format("Silver"), "{0:>30}".format(silver_name), "{0:>20.2f}".format(silver_score))
print("{0:<10}".format("Bronze"), "{0:>30}".format(bronze_name), "{0:>20.2f}".format(bronze_score))

