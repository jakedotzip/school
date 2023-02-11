def compare():
    lenA = int(input("Enter length of rectangle A: "))
    widA = int(input("Enter width of rectangle A: "))
    lenB = int(input("Enter length of rectangle B: "))
    widB = int(input("Enter width of rectangle B: "))
    areaA = lenA * widA
    areaB = lenB * widB
    print("Area A:", areaA)
    print("Area B:", areaB)
    if(areaA == areaB):
        print("Area A is equal to Area B")
    elif(areaA > areaB):
        print("Area A is greater than Area B")
    else:
        print("Area B is greater than Area A")
compare()