# Задание №7
# � Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами от 1 до 100.
# � При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения вычислений.

import asyncio
from random import randint
import time


async def calc_sum(arr_1, arr_2):
    sum_value = 0
    for n in arr_1:
        sum_value += n
    arr_2.append(sum_value)


async def main():
    nums = []
    for _ in range(1, 1_000_000):
        nums.append(randint(1, 100))
    task_num = 4
    section_size = int(len(nums)/task_num)
    section_sums = []
    tasks = []
    for i in range(0, len(nums), section_size):
        section = nums[i:i + section_size]
        task = asyncio.ensure_future(calc_sum(section, section_sums))
        tasks.append(task)
    await asyncio.gather(*tasks)

    overall_sum = 0
    for i in section_sums:
        overall_sum += i
    print(f'Sum: {overall_sum}')


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print(f'Time: {time.time() - start_time}')


# Результат:    2 подзадачи = 0.8 сек
#               4 подзадачи = 0.8 сек
#               8 подзадач = 0.8 сек

