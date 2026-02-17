# Правильный многоугольник

from math import pi, pow, tan

n, a = int(input()), float(input())
print((n * pow(a,2)) / (4 * tan(pi/n)))


