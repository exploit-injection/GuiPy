import hashlib
import os
from os import listdir

# Функция для получения хеш-суммы файла


def hash_file(file_name):
    h = hashlib.sha256()  # Создание объекта хеша

    #  Открытие файла для чтения в двоичном режиме
    # check = os.path.exists(file_name)
    # print(check) - проверка файла на существование
    with open(file_name, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)  # Циклом читаем до конца файла только 1024 байта за раз
            h.update(chunk)

    return h.hexdigest()


dir_hash = ''

#  Распечатать все файлы и папки рекурсивно
for dirpath, dirnames, filenames in os.walk("/home/spi_729-1/Документы/Test"):
    # перебрать каталоги
    for dirname in dirnames:
        print("Каталог: ", os.path.join(dirpath, dirname))
    # перебрать файлы
    for filename in filenames:
        print("Файл: ", os.path.join(dirpath, filename))
        message = hash_file(os.path.join(dirpath, filename))
        print("Хеш-сумма: ", message)
        dir_hash += message

print(hashlib.sha256(dir_hash.encode('utf8')).hexdigest())
