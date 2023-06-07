import hashlib
import os  # для отображения содержимого директории
import sys  # sys нужен для передачи argv в QApplication

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
        self.btnControl.clicked.connect(self.control_files)  # инициализация для метода по нажатию кнопки "Добавить на КЦ"
        self.pushButton_3.clicked.connect(self.check_files) # инициализация для метода по нажатию кнопки "Проверить КЦ"

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
        # print(item_text_list)
        try:
            with open("out.txt", "w") as files_control:
                for file in item_text_list:
                    if os.path.exists(file) and os.path.isfile(file):
                        file_hash = hash_file(file)
                        item = icons('./icons/file.png', file)
                        self.listWidgetControl.addItem(item)  # Добавление файлов в поле "Файлы на КЦ"
                        file_tuple = (file, file_hash)
                        print(file_tuple)
                        files_control.write(f"{file_tuple}\n")
                    elif os.path.exists(file) and os.path.isdir(file):
                        dir_hash = hash_dir(file)
                        item = icons('./icons/dir.png', file)
                        self.listWidgetControl.addItem(item)  # Добавление каталогов в поле "Файлы на КЦ"
                        dir_tuple = (file, dir_hash)
                        print(dir_tuple)
                        files_control.write(f"{dir_tuple}\n")
                    else:
                        QMessageBox.information(self, 'Внимание',
                                                f'Вы не добавили файлы для контроля целостности! Повторите попытку',
                                                QMessageBox.Ok)
        except:
            QMessageBox.information(self, 'Внимание', 'Ошибка при работе с файлом!', QMessageBox.Ok)

    def check_files(self):
        file = read_files("out.txt")
        print(file)
        print(type(file))



# Функция для вывода иконок и checkbox у файлов
def icons(picture, file):
    # Создаем иконки для файлов
    item = QtWidgets.QListWidgetItem()  # определение item в QListWidget
    icon = QIcon(picture)  # добавляем иконку
    item.setIcon(icon)
    item.setCheckState(QtCore.Qt.Checked)  # устанавливаем checkbox (True)
    item.setText(file)
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
    return file_main.read()



def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    widget = QtWidgets.QWidget
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
