def calculatePerimeter(shape):
    
    if(shape == 1):
        sideLength = float(input("Enter the length of the side:"))
        return(4 * sideLength)
    
    elif(shape == 2):
        length = float(input("Enter the length of the rectangle:"))
        breadth =float(input("Enter the breadth of the rectangle:"))
        return (2 *(length+breadth))
    
    elif(shape == 3):
        sideALength = float(input("Enter the length of the a side:"))
        sideBLength = float(input("Enter the length of the b side:"))
        sideCLength = float(input("Enter the length of the c side:"))
        return (sideALength + sideBLength + sideCLength)
    
    elif(shape ==4):
        baseALength = float(input("Enter the length of the a base:"))
        baseBLength = float(input("Enter the length of the b base:"))
        sideCLength = float(input("Enter the length of the c side:"))
        sideDLength = float(input("Enter the length of the c side:"))
        return (baseALength + baseBLength + sideCLength + sideDLength)

    elif(shape == 5):
        baseLength = float(input("Enter the length of the base:"))
        parallelSideLength = float(input("Enter the length of one of the parallel sides:"))
        return (2 * (baseLength + parallelSideLength))

    elif(shape == 6):
        radius = float(input("Enther the length of the radius:"))
        return(2 * 3.14 * radius)
    
def calculateArea(shape):
    
    if(shape == 1):
        sideLength = float(input("Enter the length of the side:"))
        return(sideLength**2)
    
    elif(shape == 2):
        length = float(input("Enter the length of the rectangle:"))
        breadth =float(input("Enter the breadth of the rectangle:"))
        return (length * breadth )
    
    elif(shape == 3):
        baseLength = float(input("Enter the length of the base:"))
        height = float(input("Enter the height of the triangle:"))
        return ((baseLength*height) / 2)
    
    elif(shape ==4):
        baseALength = float(input("Enter the length of the a base:"))
        baseBLength = float(input("Enter the length of the b base:"))
        height = float(input("Enter the height of the trapezium:"))
        return (((baseALength + baseBLength) * height) / 2)

    elif(shape == 5):
        baseLength = float(input("Enter the length of the base:"))
        height = float(input("Enter the height of the parallelogram:"))
        return (baseLength * height)

    elif(shape == 6):
        radius = float(input("Enther the length of the radius:"))
        return(3.14 * radius**2)
    
stop = False

while (stop == False):
    print( "Choose the 2D shape:\n1-Square\n2-Rectangle\n3-Triangle\n4-Trapezium\n5-Parallelogram\n6-Circle\n0-break")
    chosenShape = int(input())
    print()
    
    if(chosenShape == 0):
        stop = True

    elif(chosenShape > 6):
        print("Choose the correct shape!\n")
    
    else:
        print( "What do you want to calculate?:\n1-Perimeter\n2-Area\n0-Change shape")
        whatToCalculate = int(input())
        print()
        
        if(whatToCalculate == 0):
            continue

        elif(whatToCalculate == 1):
            p = calculatePerimeter(chosenShape)
            print("The perimeter is:",p,"\n")
            
        elif(whatToCalculate == 2):
            c = calculateArea(chosenShape)
            print("The area is:",c,"\n")

        else:
            print("Choose the correct value to calculate!\n")


