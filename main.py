import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

import control  # конвертированный файл дизайна
import os  # для отображения содержимого директории


class ExampleApp(QtWidgets.QMainWindow, control.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле control.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации дизайна
        self.btnChoosedir.clicked.connect(self.choose_dir)  # инициализация для метода по нажатию кнопки "Добавить каталог"
        self.btnChoosefile.clicked.connect(self.choose_file)  # инициализация для метода по нажатию кнопки "Добавить файлы"
        self.btnDel.clicked.connect(self.delete_item)  # инициализация для метода по нажатию кнопки "Удалить файлы"

    # Функция для выбора каталога
    def choose_dir(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории

        # перебор элементов в окне выбора файлов
        itemtextlist = [str(self.listWidgetChoose.item(i).text()) for i in range(self.listWidgetChoose.count())]



        # Вывести в окно все файлы и папки рекурсивно
        for dir_path, dir_names, file_names in os.walk(directory):

            # перебрать каталоги
            for dir_name in dir_names:
                dir = os.path.join(dir_path, dir_name)
                if dir in itemtextlist:
                    QMessageBox.information(self, 'Внимание', f'Ранее каталог {dir} и все его файлы были добавлены', QMessageBox.Ok)
                else:
                    self.listWidgetChoose.addItem(dir)

            # перебрать файлы
            for file_name in file_names:
                file = os.path.join(dir_path, os.path.join(dir_path, file_name))
                if file in itemtextlist:
                    return  # так как с QMessageBox будет выводиться очень много окон
                else:
                    self.listWidgetChoose.addItem(file)

    # Функция выбора файла
    def choose_file(self):
        files, x = QtWidgets.QFileDialog.getOpenFileNames(self, 'Выберите файлы', '/home/spi_729-1/Документы')

        for file in files:
            # Проверка на существование файла в окне выбора
            itemtextlist = [str(self.listWidgetChoose.item(i).text()) for i in range(self.listWidgetChoose.count())]  # перебор элементов в окне выбора файлов
            if file in itemtextlist:
                QMessageBox.information(self, 'Внимание', f'Ранее файл {file} был добавлен', QMessageBox.Ok)
            else:
                self.listWidgetChoose.addItem(file)  # выводим название файла и полный его путь

    # Функция удаления файлов из списка
    def delete_item(self):
        list_items = self.listWidgetChoose.selectedItems()
        if not list_items:
            QMessageBox.information(self, 'Внимание', f'Вы не выбрали файл для удаления! Повторите попытку', QMessageBox.Ok)
        for item in list_items:
            self.listWidgetChoose.takeItem(self.listWidgetChoose.row(item))










def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()