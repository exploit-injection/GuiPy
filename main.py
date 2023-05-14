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
        self.btnDel.clicked.connect(self.delete_item)

    def choose_dir(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории

        if directory: # не продолжать выполнение, если пользователь не выбрал директорию
            for file_name in os.listdir(directory):  # для каждого файла в директории
                self.listWidgetChoose.addItem(file_name)  # добавить файл в textFileChoose

    def choose_file(self):
        files, x = QtWidgets.QFileDialog.getOpenFileNames(self, 'Выберите файлы', '/home', 'txt file (*.txt);;jpg file (*.jpg)')
        #print(count)
        for file in files:
            # path = file  # определяем полный путь к файлу
            # dirpath, filename = os.path.split(path)  # отделяем путь к файлу и название файла


            # Проверка на существование файла в окне выбора
            itemtextlist = [str(self.listWidgetChoose.item(i).text()) for i in range(self.listWidgetChoose.count())]  # перебор элементов в окне выбора файлов
            if file in itemtextlist:
                QMessageBox.information(self, 'Внимание', f'Ранее файл {file} был добавлен', QMessageBox.Ok)
            else:
                self.listWidgetChoose.addItem(file)  # выводим название файла и полный его путь

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