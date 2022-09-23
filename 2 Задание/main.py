#2 Задание

import random

distance = 100
amountMeasurements = 50
error = 2
measurements = set()
sum = 0

for i in range(50):
    num = round(random.uniform(98, 102),1)
    measurements.add(num)
    if i == 0:
        minimum = num
        maximum = num
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

print('Количество элементов множества: ', len(measurements))
print('Самый большой элемент множества: ', maximum)
print('Самый маленький элемент множества: ', minimum)

measurements.remove(maximum)
measurements.remove(minimum)

for i in measurements:
    sum += i

mean = sum / len(measurements)
print('Среднее значение замера: ', mean)