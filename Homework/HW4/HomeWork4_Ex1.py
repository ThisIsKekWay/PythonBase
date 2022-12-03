# Вычислить число ПИ c заданной точностью d
import math

d = float(input('Введите желаемую точность '))
counter = 0
while d < 1:
    d *= 10
    counter += 1

pi_str = str(math.pi)
print(pi_str[:counter + 2])
