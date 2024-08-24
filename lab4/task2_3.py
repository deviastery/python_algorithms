# -*- coding: cp1251 -*-
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))
        
    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        raise KeyError("Ключ не найден в таблице.")
    
    def delete(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return
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