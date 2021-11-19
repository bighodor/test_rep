# Главный файл проекта
from file2 import data
from file3 import another_data


def func_main(data, another_data):
    res = []  # Список для хранения результатов
    for element in data:
        if element in another_data:
            res.append(element)  # Добавление элемента в результирующий список
    return element


res = func_main(data, another_data)
print(f"Результат:\n"
      f"{res}")
