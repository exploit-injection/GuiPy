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
        for rows in range(self.listWidgetChoose.count()):
            print(rows)
            item_checked = self.listWidgetChoose.item(rows).checkState()
            #print(item)
            #print(item.checkState())  # 0 на неотмеченных
            if item_checked == QtCore.Qt.CheckState.Unchecked:
                print("No")
                self.listWidgetChoose.takeItem(self.listWidgetChoose.currentRow())

        # list_items = self.listWidgetChoose.selectedItems()
        # if not list_items:
        #     QMessageBox.information(self, 'Внимание', f'Вы не выбрали файл для удаления! Повторите попытку',
        #                             QMessageBox.Ok)
        # for item in list_items:
        #     self.listWidgetChoose.takeItem(self.listWidgetChoose.row(item))

    def control_files(self):
        item_text_list = [str(self.listWidgetChoose.item(i).text()) for i in
                          range(self.listWidgetChoose.count())]  # перебор элементов в окне выбора файлов
        self.listWidgetControl.clear()  # очищение поля "Файлы на КЦ"
        # print(item_text_list)
        for file in item_text_list:

            if os.path.exists(file) and os.path.isfile(file):
                file_hash = hash_file(file)
                item = icons('./icons/file.png', file)
                self.listWidgetControl.addItem(item)  # Добавление файлов в поле "Файлы на КЦ"
                print(file, file_hash)
            elif os.path.exists(file) and os.path.isdir(file):
                dir_hash = hash_dir(file)
                item = icons('./icons/dir.png', file)
                self.listWidgetControl.addItem(item)  # Добавление каталогов в поле "Файлы на КЦ"
                print(file, dir_hash)
            else:
                QMessageBox.information(self, 'Внимание',
                                        f'Вы не добавили файлы для контроля целостности! Повторите попытку',
                                        QMessageBox.Ok)


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


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
