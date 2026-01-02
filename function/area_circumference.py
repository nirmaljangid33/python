import math

def circle(redius):
    area = math.pi*redius**2
    circum = 2*math.pi*redius
    return area, circum

a,b = circle(3)
print("area is : ", round(a,2), "circumference :" ,round(b,2))
