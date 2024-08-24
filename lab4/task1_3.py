# -*- coding: cp1251 -*-
# 2 в n
import random

def generate_random_array(length):
    random_array = [random.randint(1, 100) for _ in range(length)]
    return random_array

def fibonacci_search(arr, x):
    n = len(arr)
    
    fib1 = 0
    fib2 = 1
    fib = fib1 + fib2
    
    while fib < n:
        fib1 = fib2
        fib2 = fib
        fib = fib1 + fib2
    
    offset = -1
    
    while fib > 1:
        i = min(offset + fib1, n - 1)
        
        if arr[i] < x:
            fib = fib2
            fib2 = fib1
            fib1 = fib - fib2
            offset = i
        
        elif arr[i] > x:
            fib = fib1
            fib2 -= fib1
            fib1 -= fib2
        
        elif arr[i] == x:
            return i
    
    if fib2 and arr[offset+1] == x:
        return offset+1
    
    return -1

def fibonacci_delete(arr, target):

    index = fibonacci_search(arr, target)

    if index != -1:
        arr.pop(index)
        return arr
    else:
        return False
    
def fibonacci_insert(arr, target):
    fib1 = 0
    fib2 = 1
    while fib2 < target:
        fib1 = fib2
        fib2 = fib1 + fib2

    arr.append(target)

    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
        else:
            break

    return arr

length = 10
arr = sorted(generate_random_array(length))
print(arr)
target = 13

# вставка элемента

result = fibonacci_insert(arr, target)
print(result)

# поиск элемента
result_index = fibonacci_search(result, target)

if result_index != -1:
    print(f"Элемент {target} найден в индексе {result_index}.")
else:
    print(f"Элемент {target} не найден в массиве.")

# удаление элемента

if fibonacci_delete(result, target):
    print(f"Элемент {target} удален из массива.")
    print(result)
else:
    print(f"Элемент {target} не найден в массиве.")

