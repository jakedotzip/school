a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
def sum():
    total = 0
    for i in range(a,b+1):
        print(i, end=' ')
        total += i
    return total
print("\nsum of numbers:  " + str(sum()))