# first_name = input()
# last_name = input()
# age = int(input())
# town = input()

# print(f'You are {0} {1}, a {2}-years old person from {3}.'.format(first_name, last_name, age, town))

# first_name = input()
# last_name = input()
# age = int(input())
# town = input()

# print(
#     "You are {0} {1}, a {2}-years old person from {3}.".format(
#         first_name, last_name, age, town
#     )
# )
# print("price = %.2f \nVAT = %.3f" % (1.60,1.60 * 0.2))
# import math

# r = float(input("Enter circle radius => r= "))

# area = math.pi * r**2
# perimeter = 2 * math.pi * r
# print("Area = %.2f" % area)
# print("Perimeter = %.2f" % perimeter)

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

width = max(x1, x2) - min(x1, x2)
height = max(y1, y2) - min(y1, y2)

area = width * height
perimeter = 2 * (width + height)

print("Area = ", area)
print("Perimeter = ", perimeter)
