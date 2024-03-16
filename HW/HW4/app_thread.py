# Задание №7
# � Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами от 1 до 100.
# � При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения вычислений.

import threading
from random import randint
import time


nums = []
for _ in range(1, 1_000_000):
    nums.append(randint(1, 100))
section_sums = []


def calc_sum(list_):
    global section_sums
    sum_value = 0
    for n in list_:
        sum_value += n
    section_sums.append(sum_value)


thread_num = 10
section_size = int(len(nums)/thread_num)
threads = []
start_time = time.time()
for i in range(0, len(nums), section_size):
    section = nums[i:i + section_size]
    t = threading.Thread(target=calc_sum, args=(section,))
    threads.append(t)
    t.start()

overall_sum = 0
for i in section_sums:
    overall_sum += i

print(f'Sum: {overall_sum}')

print(f'Time: {time.time() - start_time}')

for t in threads:
    t.join()

# Результат:    50 потоков = 0.05 сек
#               100 потоков = 0.07 сек
#               1000 потоков = 0.16 сек
#
