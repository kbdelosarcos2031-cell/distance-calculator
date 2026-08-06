#"import" loads a built-in library of extra math tools
import math

#Enter the first Values of
x1=float(input("Enter value of x1: "))
y1=float(input("Enter value of y1: "))

x2=float(input("Enter value of x2: "))
y2=float(input("Enter value of y2: "))

part_x=math.pow(x1-x2,2)
part_y=math.pow(y1-x2,2)

distance=math.sqrt(part_x+part_y)

print (f"\nThe distance between the two points is:", distance)


"""
Using a library is more practical than writing all equations because it helps you save time and cost low effort,
it also makes the code easy to understand and not as complex as using calculations.

"""
