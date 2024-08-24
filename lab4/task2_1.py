# -*- coding: cp1251 -*-

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = (key, value)
        else:
            new_index = (index + 1) % self.size
            while new_index != index:
                if self.table[new_index] is None:
                    self.table[new_index] = (key, value)
                    return
                new_index = (new_index + 1) % self.size
            raise Exception("Хэш-таблица заполнена.")

    def search(self, key):
        index = self.hash_function(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start_index:
                break
        raise KeyError("Ключ не найден в таблице.")

    def delete(self, key):
        index = self.hash_function(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return
            index = (index + 1) % self.size
            if index == start_index:
                break
        raise KeyError("Ключ не найден в таблице.")

# Пример использования
hash_table = HashTable(10)
hash_table.insert(3, "значение1")
hash_table.insert(13, "значение2")
hash_table.insert(23, "значение3")

print(hash_table.search(3))  # Выведет: значение1

hash_table.delete(3)
try:
    print(hash_table.search(3))
except KeyError as e:
    print("Ключ не найден в таблице.")
