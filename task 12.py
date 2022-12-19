# Задача 12
# Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике.
#  Он задумывает два натуральных числа X и Y (X,Y≤1000),
#  а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

import random
n = int(input('x = от 0 до '))
N = int(input('y = от 0 до '))
x = round(random.randint(0,n))
y = round(random.randint(0,N))
print('x:', x, 'y:', y, sep='\n')

sum = x + y
composition = x * y
print('сумма:', sum, 'произведение:', composition)

for i in range(0,n):
    for j in range(0,N):
        if (i*j == composition) & (i + j == sum):
            print('x  = {};y = {}'.format(i,j))
           

