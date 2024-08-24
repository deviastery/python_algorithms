# -*- coding: cp1251 -*-
#O(log(log(n)))
import random

def generate_random_array(length):
    random_array = [random.randint(1, 100) for _ in range(length)]
    return random_array

def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high and arr[low] <= target <= arr[high]:
        pos = low + ((high - low) // (arr[high] - arr[low])) * (target - arr[low])
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    
    return -1

def interpolation_delete(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                arr.pop(low)
            break

        pos = low + ((high - low) // (arr[high] - arr[low])) * (target - arr[low])

        if arr[pos] == target:
            arr.pop(pos)
            high -= 1
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return arr
    
def interpolation_insert(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high and arr[low] <= target <= arr[high]:
        pos = low + ((high - low) // (arr[high] - arr[low])) * (target - arr[low])
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    
    arr.insert(low, target)
    return low


length = 10
arr = sorted(generate_random_array(length))

target = 13

print(arr)

# вставка элемента

interpolation_insert(arr, target)
print(f"Элемент {target} успешно вставлен.")
print(arr)

# поиск элемента
result = interpolation_search(arr, target)

if result != -1:
    print(f"Элемент {target} найден в индексе {result}.")
else:
    print(f"Элемент {target} не найден в массиве.")

# удаление элемента

if interpolation_delete(arr, target):
    print(f"Элемент {target} удален из массива.")
    print(arr)
else:
    print(f"Элемент {target} не найден в массиве.")


