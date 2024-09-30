import math as m
from variables_for_RSA import *
import random


def inverse(a: int, m: int) -> int:
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


def gcd(a: int, b: int) -> int:
    return a if b == 0 else m.gcd(a, a % b)


def generate_keypair(p, q, bit_length):

    p = gen_prime(bit_length)
    q = gen_prime(bit_length)

    n = p * q
    phi = (p-1) * (q-1)

    # Выбираем открытый ключ e, такой что 1 < e < phi и e взаимно прост с phi
    e = random.randrange(2, phi)
    while m.gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Вычисляем закрытый ключ d, такой что d * e ≡ 1 (mod phi)
    d = inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    
    return ciphertext



def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plaintext)


def running():
    print("RSA is running...")


def extract_data(file_path):
    with open(file_path, 'r') as file:
        content1 = file.readline()
        content2 = file.readline()

    # Удаляем скобки "(" и ")"
    content1 = content1.replace('(', '').replace(')', '')
    content2 = content2.replace('(', '').replace(')', '')

    print(content1, "\n\n", content2)
    # Разделяем данные по квадратным скобкам
    data1 = content1.split('[')[1].split(']')[0].split(", ")
    data2 = content2.split('[')[1].split(']')[0].split(", ")

    res1 = [int(item) for item in data1]
    res2 = [int(item) for item in data2]

    return res1, res2

def gen_key_data():
    p = gen_prime(1024)
    q = gen_prime(1024)

    public, private = generate_keypair(p, q, 1024)
    # print(f'Public key: [{public}]\nPrivate key: [{private}]')
    with open("res\\keys_for_RSA.txt", mode = "w") as f_key:
        print(type(public))
        f_key.write(f'Public key: [{public}]\nPrivate key: [{private}]')
    
    return p, q, public, private


def read_numbers_from_file(filename):
    numbers = []
    with open(filename, "r") as file:
        line = file.read()  # Считываем весь файл в строку
        parts = line.split(", ")  # Разбиваем строку на части по разделителю
        for part in parts:
            try:
                number = int(part)  # Преобразуем строку в целое число
                numbers.append(number)  # Добавляем число в список
            except ValueError:
                print(f"Не удалось преобразовать '{part}' в число. Пропустим его.")

    return numbers