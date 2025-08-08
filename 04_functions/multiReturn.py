def calcAreaAndCircum(r):
    area=3.14*r*r
    circum=2*3.14*r
    return area, circum

r=int(input("Enter radius: "))
area, circum = calcAreaAndCircum(r)
print("Area is: ", area)
print("Circumference is: ", circum)