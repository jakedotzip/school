num = int(input("Enter a number: "))
def sumOdd():
    odd = 0
    for i in range(1,num+1):
        if (i%2 == 1):
            odd += i
    return odd
def sumEven():
    even = 0
    for i in range(1,num+1):
        if (i%2 == 0):
            even += i
    return even
print("sum of odd numbers:  ", sumOdd())
print("sum of even numbers:  ", sumEven())
