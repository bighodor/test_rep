# Главный файл проекта
from file2 import data
from file3 import another_data
import math as m


def func_main(data, another_data):
    buf = m.sin(2)
    res = []  # Список для хранения результатов
    for element in data:
        if element in another_data:
            res.append(element)  # Добавление элемента в результирующий список

    return element


res = func_main(data, another_data)
print(f"Результат равен:\n"
      f"{res}.\n"
      f"Точно {res}?\n"
      f"Точно!")
