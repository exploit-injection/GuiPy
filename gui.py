from PyQt5 import QtWidgets  # Подключение класса для создания графических объектов
from PyQt5.QtWidgets import QApplication, QMainWindow  # Позволяют создать приложение и главное окно программы
import sys


#  Создание нового класса. Наследование от QMainWindow
class Window(QMainWindow):
    # Создание конструктора - вызывается каждый раз при создании объекта на основе этого класса
    def __init__(self):
        #  Вызов конструктора, который внутри класса QMainWindow
        super(Window, self).__init__()

        self.setWindowTitle("Новая программа")
        self.setGeometry(300, 250, 350, 200)  # Указание расположения окна, ширины и высоты

        self.new_text = QtWidgets.QLabel(self)  # Создание нового объекта (переменной) типа Label
        #  Создание переменных, которые принадлежат классу Window
        self.main_text = QtWidgets.QLabel(self)  # Запрашиваем объект - label
        self.main_text.setText("Это базовая надпись")
        self.main_text.move(100, 100)  # Делаем отступ надписи
        self.main_text.adjustSize()  # Подстраиваем ширину объекты под его содержимое

        #  Создание кнопки
        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText("Нажми, прошу")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.add_label)

    def add_label(self):
        self.new_text.setText("Привет, медвед!!!")  # Обращение к объекту new_text
        self.new_text.adjustSize()


def application():
    app = QApplication(sys.argv)  # Обращение к настройкам для создания приложения
    window = Window()  #  Создание объекта класса Window

    window.show()  # See window
    sys.exit(app.exec_())  # Для корректного завершения программы


#  Вызов метода
if __name__ == "__main__":
    application()
