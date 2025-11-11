import math
def square(side):
    return math.ceil(side*side)

side_num = float(input ("введите сторону: "))
print(f"Площадь равна: {square(side_num)}")