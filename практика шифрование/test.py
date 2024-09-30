# from RSA import *
# from variables_for_RSA import *
# import time


# if __name__ == "__main__":
#     running()

#     command = input('Do you want to chande standart bit_length = 1024? [Y/N]:  ')
#     print("Generating public/private keypair...")
    
#     while command not in 'YN':
#         print('Invalid input')
#         command = input("Do you want to chande standart bit_length = 1024? [Y/N]:  ")
#     if command == 'Y':
#         bit_length = int(input("Enter bit length: "))
#     else:
#         print('Generating keys using standart bit_length = 1024...')


#     p = gen_prime(bit_length)
#     q = gen_prime(bit_length)
    

#     public, private = generate_keypair(p, q, bit_length)
#     print(f'Public key: [{public}]\nPrivate key: [{private}]')
    

#     message = input('Enter message to ecnrypt:  ')
#     encrypted_message = encrypt(public, message)
#     print("Encrypted message:", encrypted_message)

#     decrypted_message = decrypt(private, encrypted_message)
#     print("Decrypted message:", decrypted_message)

#     # time.sleep(5000)


# # if __name__ == "__main__":
# #     alph = ''

# #     for i in range(36):
# #         if i > 9:
# #             alph += str(chr(i + 55))
# #         else:
# #             alph += str(i)

# #     arr = []
# #     print(alph)

# #     for x in alph:
# #         for y in alph:
# #             temp = int(f'21{x}457{y}9', 37)
# #             if temp % 36 == 0:
# #                 arr.append(int(f'{x}{y}', 37))

# #     print(arr)


# # def extract_data(file_path):
# #     with open(file_path, 'r') as file:
# #         content1 = file.readline()
# #         content2 = file.readline()

# #     # Удаляем скобки "(" и ")"
# #     content1 = content1.replace('(', '').replace(')', '')
# #     content2 = content2.replace('(', '').replace(')', '')

# #     print(content1, "\n\n", content2)
# #     # Разделяем данные по квадратным скобкам
# #     data1 = content1.split('[')[1].split(']')[0].split(", ")
# #     data2 = content2.split('[')[1].split(']')[0].split(", ")

# #     res1 = [int(item) for item in data1]
# #     res2 = [int(item) for item in data2]

# #     return res1, res2

# # # Пример использования
# # file_path = 'res\\keys_for_RSA.txt' # Замените 'your_file.txt' на имя вашего файла
# # public_key, private_key = extract_data(file_path)
# # print(f"Public key: {public_key}")
# # print(f"Private key: {private_key}")


# import decimal

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

# Пример использования:
numbers = read_numbers_from_file("C:\\Users\\79045\\Desktop\\encode rsa.txt")
print(numbers)