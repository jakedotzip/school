def inCircle():
    x = int(input("Enter x coordinate: "))
    y = int(input("Enter y coordinate: "))
    r = int(input("Enter r coordinate: "))

    if (x**2 + y**2 <= r**2):
        print("Point (", x, ",", y, ") is in circle with radius ", r)
    else:
        print("Point (", x, ",", y, ") is not in circle with radius ", r)
inCircle()