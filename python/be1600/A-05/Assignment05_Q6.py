n=7

print("first nested loop")
for i in range(n+1):
    for j in range(i):
        print ('*', end="")
    print('')

print("\nsecond nested loop\n")
for i in range(n,0,-1):
    for j in range(i):
        print('*', end="")
    print('')