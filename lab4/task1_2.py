# -*- coding: cp1251 -*-
# Olog(n)
import random

def generate_random_array(length):
    random_array = [random.randint(1, 100) for _ in range(length)]
    return random_array

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(node, result):
    if node:
        inorder_traversal(node.left, result)
        result.append(node.value)
        inorder_traversal(node.right, result)

def print_tree(root):
    result = []
    inorder_traversal(root, result)
    print(result)

def build_binary_search_tree(arr):
    if not arr:
        return None

    mid = len(arr) // 2
    root = Node(arr[mid])
    root.left = build_binary_search_tree(arr[:mid])
    root.right = build_binary_search_tree(arr[mid + 1:])

    return root

def binary_tree_search(node, target):
    if not node or node.value == target:
        return node

    if target < node.value:
        return binary_tree_search(node.left, target)
    else:
        return binary_tree_search(node.right, target)

def find_min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def binary_tree_delete(root, target):
    if not root:
        return root

    if target < root.value:
        root.left = binary_tree_delete(root.left, target)
    elif target > root.value:
        root.right = binary_tree_delete(root.right, target)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        temp = find_min_value_node(root.right)
        root.value = temp.value
        root.right = binary_tree_delete(root.right, temp.value)

    return root

def insert_node(root, target):
    if not root:
        return Node(target)

    if target < root.value:
        root.left = insert_node(root.left, target)
    else:
        root.right = insert_node(root.right, target)

    return root


length = 10
arr = sorted(generate_random_array(length))

root = build_binary_search_tree(arr)
target = 13

print_tree(root)

# вставка элемента
root = insert_node(root, target)

if root:
    print(f"Элемент {target} добавлен в бинарное дерево.")
else:
    print(f"Ошибка при добавлении элемента {target} в бинарное дерево.")

print_tree(root)

# поиск элемента
result_node = binary_tree_search(root, target)

if result_node:
    print(f"Элемент {target} найден в бинарном дереве.")
else:
    print(f"Элемент {target} не найден в бинарном дереве.")

# удаление элемента
root = binary_tree_delete(root, target)

if root:
    print(f"Элемент {target} удален из бинарного дерева.")
else:
    print(f"Элемент {target} не найден в бинарном дереве.")

print_tree(root)
