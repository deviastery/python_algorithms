# -*- coding: cp1251 -*-
# O(logn)
import random

def generate_random_array(length):
    random_array = [random.randint(1, 100) for _ in range(length)]
    return random_array

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Если элемент в середине массива равен целевому значению, возвращаем его индекс
        if arr[mid] == target:
            return mid
        # Если целевое значение меньше элемента в середине массива, ищем слева от середины
        elif arr[mid] > target:
            right = mid - 1
        # Если целевое значение больше элемента в середине массива, ищем справа от середины
        else:
            left = mid + 1

    # Если элемент не найден, возвращаем -1
    return -1

def binary_delete(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Если элемент в середине массива равен целевому значению, удаляем его и возвращаем True
        if arr[mid] == target:
            arr.pop(mid)
            return True
        # Если целевое значение меньше элемента в середине массива, ищем слева от середины
        elif arr[mid] > target:
            right = mid - 1
        # Если целевое значение больше элемента в середине массива, ищем справа от середины
        else:
            left = mid + 1

    # Если элемент не найден, возвращаем False
    return False

def binary_insert(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            # Если элемент уже существует в массиве, вставляем его на текущую позицию
            arr.insert(mid, target)
            return arr
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Если элемент не найден, добавляем его в подходящую позицию
    arr.insert(left, target)
    return arr

length = 10
arr = sorted(generate_random_array(length))

target = 13

# вставка элемента
new_arr = binary_insert(arr, target)

print(new_arr)

# поиск элемента
result = binary_search(arr, target)

if result != -1:
    print(f"Элемент {target} найден в индексе {result}.")
else:
    print(f"Элемент {target} не найден в массиве.")

# удаление элемента
if binary_delete(arr, target):
    print(f"Элемент {target} удален из массива.")
else:
    print(f"Элемент {target} не найден в массиве.")

print(arr)

