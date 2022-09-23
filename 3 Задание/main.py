#3 Задание

import copy
import random

shop_1 = {'сыр':[100, 10],
          'рыба':[280, 7],
          'арбуз':[80, 18],
          'огурец':[40, 20],
          'колбаса':[300, 40],
          'помидор':[60, 16],
          'молоко':[80, 7],
          'кефир':[70, 12],
          'хлеб':[30, 5],
          'плюшка':[30, 8],}

shop_2 = copy.deepcopy(shop_1)

print('Словарь shop_2 начальный: ', shop_2)

for _ in range(2):
    shop_2.pop(random.choice(list(shop_2.keys())))

for i in shop_2:
    randPrice = random.randint(0, 500)
    randAmountDays = random.randint(0,40)
    shop_2.update({i:[randPrice, randAmountDays]})

shop_2['курица'] = [190, 20]
shop_2['ветчина'] = [140, 39]

print('Словарь shop_2: ', shop_2)

counter = 0
theBestPrice = {}

for i in shop_2:
    if counter == 3:
        break
    if shop_1.get(i):
        counter += 1
        if shop_1[i][1] > shop_2[i][1]:
            theBestPrice[i] = ['shop_1', shop_1[i][0], shop_1[i][1]]
        elif shop_1[i][1] < shop_2[i][1]:
            theBestPrice[i] = ['shop_2', shop_2[i][0], shop_2[i][1]]
        else:
            theBestPrice[i] = ['shop_1 и shop_2', shop_2[i][0], shop_2[i][1]]

print('Словарь shop_1: ', shop_1)
print('Словарь с лучшим сроком годности:', theBestPrice)

