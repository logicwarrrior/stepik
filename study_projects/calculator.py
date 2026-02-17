from math import pi, pow, tan, sin, cos, sqrt

# # Правильный многоугольник
# n, a = int(input()), float(input())
# print((n * pow(a,2)) / (4 * tan(pi/n)))
#
#
# #Средние значения
# s, b = float(input()), float(input())
# print((s + b) / 2)
# print(sqrt(s * b))
# print((2 * s * b) / (s + b))
# print(sqrt((pow(s, 2) + pow(b, 2)) / 2))

from math import pow, sqrt
a, b, c = float(input()), float(input()), float(input())
d = pow(b, 2) - 4 * a * c

if d < 0:
    print('Нет корней')
elif d == 0:
    print(-b / (2 * a))
else:
    print((-b - sqrt(d))/(2 * a))
    print((-b + sqrt(d))/(2 * a))

