import math

#define a function triangleArea(base, height)
def triangleArea(base,height):
    area = 0.5*base*height
    return area
#define a function spiralArea(numberOfTriangles)
def spiralArea(numberOfTriangles):
    leg = 1
    areaOfTriangle = triangleArea(1,1)
    totalArea = areaOfTriangle
    hypotenuse = math.hypot(1,1)
    areaSpiral = areaOfTriangle
    
    #Construct a loop to deal with the next triangle. It will deal with every next triangle up until and including the last one.
    for i in range(1,numberOfTriangles):
        leg = hypotenuse
        areaOfTriangle = triangleArea(leg,leg)
        hypotenuse = math.hypot(leg,leg)
        totalArea = totalArea + areaOfTriangle
        print(f"The area of the spiral after {i} triangles is {round(totalArea,1)}.")
        
#Invoke, or call the spiralArea function. Plug in the number of triangles you want to use.
whatIsTheSpiralArea = spiralArea(28)


