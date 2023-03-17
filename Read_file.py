#  Создание переменной, в которой путь к файлу
inputfile = "../password.txt"
# Открытие файла. Выбор в каком режиме открыть файл. Пока только чтение
myfile = open(inputfile, mode='r', encoding='latin_1')
# Чтение файла, который был указан
# print(myfile.read())

for num, line in enumerate(myfile, 1):
    #  Вывод всех паролей, в которых есть vasya
    if "vasya" in line:
        print("Line № " + str(num) + ": " + line.strip())
