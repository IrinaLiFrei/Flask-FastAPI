# Задание №7
# � Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами от 1 до 100.
# � При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения вычислений.

import multiprocessing
from random import randint
import time


def calc_sum(arr_1, arr_2):
    sum_value = 0
    for n in arr_1:
        sum_value += n
    arr_2.append(sum_value)


if __name__ == '__main__':
    processes = []
    nums = []
    for _ in range(1, 1_000_000):
        nums.append(randint(1, 100))
    process_num = 2
    section_size = int(len(nums)/process_num)
    start_time = time.time()

    section_sums = multiprocessing.Manager().list()
    for i in range(0, len(nums), section_size):
        section = nums[i:i + section_size]
        p = multiprocessing.Process(target=calc_sum, args=(section, section_sums))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    overall_sum = 0
    for i in section_sums:
        overall_sum += i
    print(f'Sum: {overall_sum}')

    print(f'Time: {time.time() - start_time}')


# Результат:    2 процесса = 0.5 сек
#               4 процесса = 0.7 сек
#               8 процессов = 1.17 сек

