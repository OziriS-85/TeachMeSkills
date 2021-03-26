import os
from dotenv import load_dotenv

load_dotenv()

items = os.getenv('ITEMS')
sum = os.getenv('SUM')
order_num = os.getenv('ORDER_NUM')

# 1. Касса перепутала номер в очереди с суммой. Надо поменять эти переменные местами
order_num, sum = sum, order_num

# 2. Для отчёта боссу, нужно посчитать среднюю стоимость каждой пиццы в заказе
average_cost = sum // items

# 3. Если в сумме заказа нету дробей (.00), нужно, чтобы нули не отрисовывались
if int(sum) == sum:
    sum = int(sum)
# 4. Если у клиента в номере заказа есть цифра 2, ему положена скидка в 50%
if '2' in str(n):
    print('У тебя в чеке счастливое число! Получи скидку 50%!')
    sum /= 2

# 5. Если кол-во пицц в заказе меньше 2, от номер в очереди нужно сократить на 5
if items < 2:
    if order_num > 5:
        order_num -= 5
    else:
        order_num = 1