# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

from cgitb import reset
import re


x1 = float(input('Введите координату Х1 - '))
y1 = float(input('Введите координату Y1 - '))
x2 = float(input('Введите координату Х2 - '))
y2 = float(input('Введите координату Y2 - '))

result = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (0.5)

print("{:.2f}".format(result))
