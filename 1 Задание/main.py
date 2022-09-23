#1 Задание

import random

arr = []
arrUnique = []
sum = 0
count = 0
dispersion = 0
firstPartOfExpression = 0
secondPartOfExpression = 0

for _ in range(100):
    arr.append(random.randint(0,100))

print('Начальный список: ', arr)

for index, value in enumerate(arr):
    if value < 50:
        arr[index] = 25

print('Измененный список: ', arr)

for i in arr:
    if arr.count(i) == 1:
        arrUnique.append(i)

print('Список уникальных чисел: ', arrUnique)

for i in arrUnique:
    count += 1
    sum += i

print('Математическое ожидание случайной величины: ', sum / count)

for index,value in enumerate(arrUnique):
    firstPartOfExpression += value * value * (1 / count)
    secondPartOfExpression += value * (1 / count)

    if index + 1 == len(arrUnique):
        secondPartOfExpression *= secondPartOfExpression

dispersion = firstPartOfExpression - secondPartOfExpression

print('Дисперсия: ', dispersion)
print('Минимальное число: ', min(arrUnique))
print('Максимальное число: ', max(arrUnique))
