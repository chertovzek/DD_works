from typing import List


def find_item_index(items: List, item_to_find):
    for index, item in enumerate(items):
        if item == item_to_find:
            return index
    return None  # Если товар не найден, возвращаем None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

# Цикл for нужно было перенести внутрь блока кода
for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
