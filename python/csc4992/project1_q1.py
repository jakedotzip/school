my_file = open("Project1a.txt","r")
wayne_scores = []
others_scores = []
opponent_teams = []
date = []
for line in my_file:
  line = line.strip()
  l = line.split(":")
  wayne_scores.append(int(l[2]))
  others_scores.append(int(l[4]))
  opponent_teams.append(l[3])
  date.append(l[0])
# win-loss record
win_count = 0
loss_count = 0
draw_count = 0
for i in range(len(wayne_scores)):
  if (wayne_scores[i] > others_scores[i]):
    win_count += 1
  elif (wayne_scores[i] < others_scores[i]):
    loss_count += 1
  elif (wayne_scores[i] == others_scores[i]):
    draw_count += 1
print('-'*30)
print("\tGAME RECORD:")
print("{0:<5}".format("Win -"), "{0:<5}".format(win_count), end='')
print("{0:<5}".format("Loss -"), "{0:<5}".format(loss_count), end='')
print("{0:<5}".format("Draw -"), draw_count)
print('-'*30)
# average score
wayne_avg = sum(wayne_scores)/len(wayne_scores)
others_avg = sum(others_scores)/len(wayne_scores)
print("\tAVERAGE SCORE")
print("Wayne State:", "{:.2f}".format(wayne_avg))
print("Others:", "{:.2f}".format(others_avg))
print('-'*30)
# average margin
total_winning_margin = 0
total_losing_margin = 0
for i in range(len(wayne_scores)):
  if (wayne_scores[i] > others_scores[i]):
    total_winning_margin += (wayne_scores[i]-others_scores[i])
  elif (wayne_scores[i] < others_scores[i]):
    total_losing_margin += (wayne_scores[i]-others_scores[i])
avg_winning_margin = total_winning_margin/win_count
avg_losing_margin = total_losing_margin/loss_count

print("\tAVERAGE MARGIN:")
print("Winning:", "{:.2f}".format(avg_winning_margin))
print("Losing:", "{:.2f}".format(avg_losing_margin))

# biggest win & worse defeat
game_score = []
for i in range(len(wayne_scores)):
  game_score.append(wayne_scores[i]-others_scores[i])
w_index = game_score.index(max(game_score))
l_index = game_score.index(min(game_score))
print('-'*30)
print("\tBIGGEST WIN:")
print("Match Date:", date[w_index])
print("Wayne State:", wayne_scores[w_index]) 
print(opponent_teams[w_index] + ":", others_scores[w_index])
print('-'*30)
print("\tWORSE DEFEAT:")
print("Match Date:", date[l_index])
print("Wayne State:", wayne_scores[l_index]) 
print(opponent_teams[l_index] + ":", others_scores[l_index])
print('-'*30)