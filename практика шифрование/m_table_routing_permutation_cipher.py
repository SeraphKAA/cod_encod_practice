import math

# шифр табличной маршрутной перестановки
# Этот код реализует простой шифр, который работает, записывая текст змейкой в сетку и затем считывая его обратно в том же порядке.


def enc(text):
    # Определяем размер сетки.
    n = max(5, math.ceil(math.sqrt(len(text))))

    # Создаём сетку.
    a = [['_' for _ in range(n)] for _ in range(n)]

    # Заменяем пробелы на подчёркивания.
    text = ''.join('_' if x == ' ' else x for x in text)

    t = 0

    # Заполняем сетку змейкой.
    for i in range(n):
        for j in range(n * (i % 2) - i % 2, n * ((i + 1) % 2) - i % 2, 1 - (i % 2) * 2):
            if t < len(text):
                a[j][i] = text[t]
                t += 1

    # Собираем закодированный текст.
    enctext = ''.join(''.join(row) for row in a)
    return enctext

def dec(text):
    # Определяем размер сетки.
    if math.sqrt(len(text)) <= 5:
        n = 5
    else: 
        n = math.ceil(math.sqrt(len(text)))

    # Создаем сетку.
    a = [['_' for _ in range(n)] for _ in range(n)]

    t = 0
    # Заполняем сетку по порядку.
    for i in range(n):
        for j in range(n):
            if t < len(text):
                a[i][j] = text[t]
                t += 1

    # Читаем змейкой сверху вниз, потом снизу вверх и т.д.
    dectext = ''
    for i in range(0, n):
        for j in range(n * (i % 2) - i % 2,  n * ((i + 1) % 2)  - i % 2, 1 - (i % 2) * 2):
            dectext += a[j][i]

    # Меняем подчеркивания на пробелы и обрезаем лишнее.
    dectext = dectext.replace('_', ' ').strip()
    return dectext


print("шифр табличной маршрутной перестановки is active")

# text = input("Введите текст: ")
# print("Шифрованный текст: " + enc(text))
# print("Дешифрованный текст: " + dec(enc(text)))