"""
Создайте список предметов формата Название, препод, ваша любовь к предмету(от 0 до 10).
Сохраните в CSV файл(название файла - ваша фамилия).
P.S не менее 4 столбцов.
"""
import csv
data = [
    ['ИБ', 'Кулаков С.А.', 10],
    ['Англиский', 'Жижонкова М.С.', 8],
    ['Архитектура и дизайн сетей', 'Головин В.А.', 10],
    ['фИЗРА', 'Соснин Н.А.', 10]
]

with open('EREN.csv', 'w') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)