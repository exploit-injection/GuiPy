import hashlib
import os  # для отображения содержимого директории
import shutil
import sys  # sys нужен для передачи argv в QApplication
import time
import zipfile

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

import control  # конвертированный файл дизайна


class ExampleApp(QtWidgets.QMainWindow, control.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле control.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации дизайна
        self.btnChoosedir.clicked.connect(
            self.choose_dir)  # инициализация для метода по нажатию кнопки "Добавить каталог"
        self.btnChoosefile.clicked.connect(
            self.choose_file)  # инициализация для метода по нажатию кнопки "Добавить файлы"
        self.btnDel.clicked.connect(self.delete_item)  # инициализация для метода по нажатию кнопки "Удалить файлы"
        self.btnControl.clicked.connect(
            self.control_files)  # инициализация для метода по нажатию кнопки "Добавить на КЦ"
        self.pushButton_3.clicked.connect(self.check_files)  # инициализация для метода по нажатию кнопки "Проверить КЦ"

    # Функция для выбора каталога
    def choose_dir(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку", '/home/spi_729-1/Документы')
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории

        # перебор элементов в окне выбора файлов
        item_text_list = [str(self.listWidgetChoose.item(i).text()) for i in range(self.listWidgetChoose.count())]

        # Проверка добавления основного каталога
        if directory in item_text_list:
            QMessageBox.information(self, 'Внимание', f'Ранее каталог {directory} был добавлен', QMessageBox.Ok)
        else:
            # Создаем иконки для каталога
            item = icons('./icons/dir.png', directory)
            self.listWidgetChoose.addItem(item)

        # Вывести в окно все файлы и папки рекурсивно
        for dirpath, dirnames, filenames in os.walk(directory):
            # перебрать каталоги
            for dir_name in dirnames:
                dir_res = os.path.join(dirpath, dir_name)
                if dir_res in item_text_list:
                    QMessageBox.information(self, 'Внимание', f'Ранее каталог {dir_res} был добавлен', QMessageBox.Ok)
                else:
                    # Создаем иконки для каталогов
                    item = icons('./icons/dir.png', dir_res)
                    self.listWidgetChoose.addItem(item)

            # перебрать файлы
            for file_name in filenames:
                file = os.path.join(dirpath, file_name)
                if file in item_text_list:
                    QMessageBox.information(self, 'Внимание', f'Ранее файл {file} был добавлен', QMessageBox.Ok)
                else:
                    # Создаем иконки для файлов
                    item = icons('./icons/file.png', file)
                    self.listWidgetChoose.addItem(item)

    # Функция выбора файла
    def choose_file(self):
        files, x = QtWidgets.QFileDialog.getOpenFileNames(self, 'Выберите файлы', '/home/spi_729-1/Документы')

        for file in files:
            # Проверка на существование файла в окне выбора
            item_text_list = [str(self.listWidgetChoose.item(i).text()) for i in
                              range(self.listWidgetChoose.count())]  # перебор элементов в окне выбора файлов
            if file in item_text_list:
                QMessageBox.information(self, 'Внимание', f'Ранее файл {file} был добавлен', QMessageBox.Ok)
            else:
                # Создаем иконки для файлов
                item = icons('./icons/file.png', file)
                self.listWidgetChoose.addItem(item)  # выводим название файла и полный его путь с иконкой

    # Функция удаления файлов из списка
    def delete_item(self):
        count_items = self.listWidgetChoose.count()  # Находим кол-во элементов в QListWidget
        # Проверка на заполнение QListWidget
        if count_items == 0:
            QMessageBox.information(self, 'Внимание', 'Список файлов пуст!', QMessageBox.Ok)

        check = 0
        # Если не выбраны файлы для удаления - вывод сообщения
        for rows in range(count_items):  # от 0 до 2
            item_selected = self.listWidgetChoose.item(rows)
            if item_selected.checkState() == QtCore.Qt.Checked:
                check = check + 1
        #  Сравнение check с кол-ом элементов в QListWidget
        if check == count_items and count_items != 0:
            QMessageBox.information(self, 'Внимание', 'Вы не выбрали файлы для удаления!', QMessageBox.Ok)

        #  Удаление всех выбранных элементов (не установлен checkbox)
        while check != count_items:
            for rows in range(count_items):  # от 0 до 2
                item_selected = self.listWidgetChoose.item(rows)
                if item_selected is None:
                    self.listWidgetChoose.takeItem(rows)
                elif item_selected.checkState() == QtCore.Qt.Unchecked:
                    self.listWidgetChoose.takeItem(rows)
            check = check + 1

    def control_files(self):
        item_text_list = [str(self.listWidgetChoose.item(i).text()) for i in
                          range(self.listWidgetChoose.count())]  # перебор элементов в окне выбора файлов
        self.listWidgetControl.clear()  # очищение поля "Файлы на КЦ"
        backup_file = '/home/spi_729-1/Документы/Backup'
        if os.path.exists(backup_file):
            shutil.rmtree(backup_file)
            os.makedirs(backup_file)
        else:
            os.makedirs(backup_file)
        # Добавление в файл для сравнения
        try:
            #  запись в файл данных
            with open("out.txt", "w") as files_control:
                for file in item_text_list:
                    if os.path.exists(file) and os.path.isfile(file):
                        shutil.copy2(file, backup_file) # резервное копирование файлов
                        file_hash = hash_file(file)
                        item = icons('./icons/file.png', file)
                        self.listWidgetControl.addItem(item)  # Добавление файлов в поле "Файлы на КЦ"
                        print(file, file_hash)
                        files_control.write(f"{file}, {file_hash}\n")  # Запись данных в файл
                    elif os.path.exists(file) and os.path.isdir(file):
                        backup_file = f'/home/spi_729-1/Документы/Backup/{os.path.basename(file)}'
                        # Проверка на существование файла для бэкапа
                        shutil.copytree(file, backup_file)
                        dir_hash = hash_dir(file)
                        item = icons('./icons/dir.png', file)
                        self.listWidgetControl.addItem(item)  # Добавление каталогов в поле "Файлы на КЦ"
                        print(file, dir_hash)
                        files_control.write(f"{file}, {dir_hash}\n")  # Запись данных в файл
                    else:
                        files_control.close()
                        QMessageBox.information(self, 'Внимание',
                                                f'Вы не добавили файлы для контроля целостности! Повторите попытку',
                                                QMessageBox.Ok)
        except Exception as e:
            QMessageBox.information(self, 'Внимание', 'Ошибка при работе с файлом!', QMessageBox.Ok)
            print("Ошибка", str(e))






    def check_files(self):
        out_file = read_files("out.txt")
        list_in_out_file = [i for i in out_file]  #  Список элементов в файде out.txt
        item_text_list = [str(self.listWidgetControl.item(i).text()) for i in
                          range(self.listWidgetControl.count())]  # перебор элементов в окне файлы на КЦ
        list_files = []  # Список для файлов и их хешей
        for file in item_text_list:
            if os.path.exists(file) and os.path.isfile(file):
                file_hash = hash_file(file)  # расчет хеша файлов в окне "Файлы на КЦ"
                list_files.append(f"{file}, {file_hash}")  # Добавление файла в список файлов
            elif os.path.exists(file) and os.path.isdir(file):
                dir_hash = hash_dir(file)
                list_files.append(f"{file}, {dir_hash}")  # Добавление директории в список файлов
            else:
                file = file
                file_hash = 1
                list_files.append(f"{file}, {file_hash}")  # Добавление файла в список файлов

        print(f"Список файлов: {list_files}")
        print(f"Список файлов в выходном файле: {list_in_out_file}")

        count = len(list_in_out_file)
        for item in range(count):
            file_str = str(list_files[item])  # Перевод к строке элементов в новом списке файлов и хешей
            file_res_tuple = tuple(str(item) for item in file_str.split(',') if item != '')  # Отделяем файлы и хеши в общем списке
            name_path_file, sha_hash = file_res_tuple
            if list_files[item] != list_in_out_file[item]:
                if list_files[item] == f"{name_path_file}, 1":
                    item_res_er = items_out_control('./icons/error.png', f"Нарушение КЦ файла {name_path_file}. Файл удален!", time)
                    self.listWidgetOutput.addItem(item_res_er)
                else:
                    item_res_er = items_out_control('./icons/error.png', f"Нарушение КЦ файла {name_path_file}. Файл изменен!", time)
                    self.listWidgetOutput.addItem(item_res_er)
            else:
                item_res_suc = items_out_control('./icons/success.png', f"КЦ файла {name_path_file} не нарушен", time)
                self.listWidgetOutput.addItem(item_res_suc)

        QMessageBox.information(self, 'Внимание', f'Проверка КЦ файлов успешно завершена!', QMessageBox.Ok)


        # tuple_file = self.control_files()
        # print(file)
        # print(type(file))
        # print(tuple_file)
        # list_in_out_files = [i for i in file]
        # count = len(list_in_out_files)
        # for item in range(count):
        #     file_str = str(file[item])
        #     file_res_tuple = tuple(str(item) for item in file_str.split(',') if item != '')
        #     name_path_file, sha_hash = file_res_tuple
        #     if file[item] != tuple_file[item]:
        #         item_res_er = icons('./icons/error.png', f"Нарушение КЦ файла {name_path_file}")
        #         self.listWidgetOutput.addItem(item_res_er)
        #     else:
        #         item_res_suc = icons('./icons/success.png', f"КЦ файла {name_path_file} не нарушен")
        #         self.listWidgetOutput.addItem(item_res_suc)
        # QMessageBox.information(self, 'Внимание', f'Проверка КЦ файлов успешно завершена!', QMessageBox.Ok)




# Функция для вывода иконок и checkbox у файлов
def icons(picture, file):
    # Создаем иконки для файлов
    item = QtWidgets.QListWidgetItem()  # определение item в QListWidget
    icon = QIcon(picture)  # добавляем иконку
    item.setIcon(icon)
    item.setCheckState(QtCore.Qt.Checked)  # устанавливаем checkbox (True)
    item.setText(file)
    return item

def items_out_control(picture, file, timestr):
    # Создаем иконки для файлов
    timestr = timestr.strftime("%d.%m.%Y  %H:%M:%S")
    item = QtWidgets.QListWidgetItem()  # определение item в QListWidget
    icon = QIcon(picture)  # добавляем иконку
    item.setIcon(icon)
    item.setText(f"{file}  Дата: {timestr}")
    return item

# Функция для получения хеш-суммы файла
def hash_file(file_name):
    h = hashlib.sha256()  # Создание объекта хеша

    #  Открытие файла для чтения в двоичном режиме
    with open(file_name, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)  # Циклом читаем до конца файла только 1024 байта за раз
            h.update(chunk)

    return h.hexdigest()


# Функция для получения хеш-суммы каталога
def hash_dir(dir_path):
    dir_hash = ''
    #  Распечатать все файлы и папки рекурсивно
    for dirpath, dirnames, filenames in os.walk(dir_path):
        # перебрать каталоги
        for dirname in dirnames:
            os.path.join(dirpath, dirname)  # формируем полный путь и название директории
        # перебрать файлы
        for filename in filenames:
            message = hash_file(os.path.join(dirpath, filename))  # хешируем файлы, найденные в каталоге
            dir_hash += message  # складываем хеш-суммы файлов
    return hashlib.sha256(dir_hash.encode('utf8')).hexdigest()


def read_files(files):
    file_main = open(files, "r")
    file_string = file_main.read()
    file_tuple = tuple(str(item) for item in file_string.split('\n') if item != '')  # разделила файлы по табуляции
    return file_tuple




def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
