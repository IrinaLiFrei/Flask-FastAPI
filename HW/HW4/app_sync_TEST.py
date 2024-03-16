# Задание №7
# � Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами от 1 до 100.
# � При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения вычислений.


from random import randint
import time

start_time = time.time()
nums = []
for _ in range(1, 1_000_000):
    nums.append(randint(1, 100))


def calc_sum(arr):
    sum_value = 0
    for i in arr:
        sum_value += i
    print(sum_value)


calc_sum(nums)
print(f'Time: {time.time() - start_time}')


# 0.7 сек