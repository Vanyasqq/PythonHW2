# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2


N = int(input('кол-во брошеных монет:'))

import random
list = []
for i in range(0, N):
    RandomNum = round(random.randint(0,1))
    list.append(RandomNum)
print(list)

Eagle = 0
Tails = 0

for i in range(0, N):
    if list[i] == 0:
        Eagle += 1
    else:
        Tails += 1

print('решка:{1}; орел:{0}.'.format(Eagle,Tails))

if Eagle < Tails:
    print('Монет надо перевернуть: {} ' .format(Eagle))
else:
    print('Монет надо перевернуть: {} ' .format(Tails))
