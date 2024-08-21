import math

def two_value_return(r):
    # area = (math.pi ) * (r ** 2)
    area = round((3.14) * (r ** 2), 2)
    circumference = round(2*(3.14) *( r), 2)
    return area, circumference


print(two_value_return(5))