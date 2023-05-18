import hashlib
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

import control  # конвертированный файл дизайна
import os  # для отображения содержимого директории


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
        self.btnControl.clicked.connect(self.control_files)

    # Функция для выбора каталога
    def choose_dir(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории

        # перебор элементов в окне выбора файлов
        item_text_list = [str(self.listWidgetChoose.item(i).text()) for i in range(self.listWidgetChoose.count())]

        # Проверка добавления основного каталога
        if directory in item_text_list:
            QMessageBox.information(self, 'Внимание', f'Ранее каталог {directory} был добавлен', QMessageBox.Ok)
        else:
            self.listWidgetChoose.addItem(directory)

        # Вывести в окно все файлы и папки рекурсивно
        for dirpath, dirnames, filenames in os.walk(directory):

            # перебрать каталоги
            for dir_name in dirnames:

                dir = os.path.join(dirpath, dir_name)
                if dir in item_text_list:
                    QMessageBox.information(self, 'Внимание', f'Ранее каталог {dir} был добавлен', QMessageBox.Ok)
                else:
                    self.listWidgetChoose.addItem(dir)

            # перебрать файлы
            for file_name in filenames:
                file = os.path.join(dirpath, file_name)
                if file in item_text_list:
                    QMessageBox.information(self, 'Внимание', f'Ранее файл {file} был добавлен', QMessageBox.Ok)
                else:
                    self.listWidgetChoose.addItem(file)

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
                item = QtWidgets.QListWidgetItem()
                icon = QIcon('./icons/file.png')
                item.setIcon(icon)
                item.setText(file)
                self.listWidgetChoose.addItem(item)  # выводим название файла и полный его путь с иконкой

    # Функция удаления файлов из списка
    def delete_item(self):
        list_items = self.listWidgetChoose.selectedItems()
        if not list_items:
            QMessageBox.information(self, 'Внимание', f'Вы не выбрали файл для удаления! Повторите попытку',
                                    QMessageBox.Ok)
        for item in list_items:
            self.listWidgetChoose.takeItem(self.listWidgetChoose.row(item))

    def control_files(self):
        item_text_list = [str(self.listWidgetChoose.item(i).text()) for i in
                          range(self.listWidgetChoose.count())]  # перебор элементов в окне выбора файлов
        print(item_text_list)
        for item in item_text_list:
            if os.path.exists(item) and os.path.isfile(item):
                file_hash = hash_file(item)
                print(item, file_hash)
            elif os.path.exists(item) and os.path.isdir(item):
                dir_hash = hash_dir(item)
                print(item, dir_hash)
            else:
                QMessageBox.information(self, 'Внимание',
                                        f'Вы не добавили файлы для контроля целостности! Повторите попытку',
                                        QMessageBox.Ok)


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
            print("Каталог: ", os.path.join(dirpath, dirname))
        # перебрать файлы
        for filename in filenames:
            print("Файл: ", os.path.join(dirpath, filename))
            message = hash_file(os.path.join(dirpath, filename))
            print("Хеш-сумма: ", message)
            dir_hash += message
    return hashlib.sha256(dir_hash.encode('utf8')).hexdigest()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
