# программа, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве

import math
x1 = int(input("Введите точку Х1: "))
x2 = int(input("Введите точку Х2: "))
y1 = int(input("Введите точку Y1: "))
y2 = int(input("Введите точку Y2: "))
a = round((math.sqrt((x2-x1)**2+(y2-y1)**2)),3)
print ("x = {", (x1),"; ",(x2), "} ; y = {", (y1),"; ",(y2), "} Расстояние между точками: ", (a) )