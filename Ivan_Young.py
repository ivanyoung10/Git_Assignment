# CS 16X Git Assignment

# Project requires TWO functions:
# 1. rect_area (length, width) which will return the area of a rectangle
# 2. rect_solid_area (length, width, height) which will return the area of a solid rectangular object


# Request the dimension of a solid rectangular object
length = int(input("Enter the length of the the object as in integer: "))
width = int(input("Enter the width of the the object as in integer: "))
height = int(input("Enter the height of the the object as in integer: "))

# Area function
def rect_area(x, y):
    return x * y

# Surface area function
def rect_surface_area(x, y, z):
    area = 0
    area = area + rect_area(x, y) * 2
    area = area + rect_area(x, z) * 2
    area = area + rect_area(y, z) * 2
    return area


print("Length = ", length, "Width = ", width, "Height = ", height)
print("Total Surface Area = ", rect_surface_area(length, width, height))
