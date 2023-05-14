#  Импорт необходимых модулей
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *

# Код из QTDesigner
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(217, 235, 247);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.textFileControl = QtWidgets.QTextEdit(self.centralwidget)
        self.textFileControl.setGeometry(QtCore.QRect(350, 80, 441, 231))
        self.textFileControl.setObjectName("textFileControl")
        self.textFileChoose = QtWidgets.QTextEdit(self.centralwidget)
        self.textFileChoose.setGeometry(QtCore.QRect(10, 30, 311, 351))
        self.textFileChoose.setObjectName("textFileChoose")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 390, 471, 191))
        self.groupBox.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(188, 128, 233, 255), stop:1 rgba(255, 255, 255, 255));")
        self.groupBox.setObjectName("groupBox")
        self.btnDel = QtWidgets.QPushButton(self.groupBox)
        self.btnDel.setGeometry(QtCore.QRect(1, 132, 159, 30))
        self.btnDel.setMinimumSize(QtCore.QSize(50, 30))
        self.btnDel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(133, 185, 224, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btnDel.setObjectName("btnDel")
        self.btnChoose = QtWidgets.QPushButton(self.groupBox)
        self.btnChoose.setGeometry(QtCore.QRect(1, 38, 159, 30))
        self.btnChoose.setMinimumSize(QtCore.QSize(50, 30))
        self.btnChoose.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(133, 185, 224, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btnChoose.setObjectName("btnChoose")
        self.btnRecovery = QtWidgets.QPushButton(self.groupBox)
        self.btnRecovery.setGeometry(QtCore.QRect(1, 85, 159, 30))
        self.btnRecovery.setMinimumSize(QtCore.QSize(50, 30))
        self.btnRecovery.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(133, 185, 224, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btnRecovery.setObjectName("btnRecovery")
        self.btnControl = QtWidgets.QPushButton(self.groupBox)
        self.btnControl.setGeometry(QtCore.QRect(240, 85, 159, 30))
        self.btnControl.setMinimumSize(QtCore.QSize(50, 30))
        self.btnControl.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(133, 185, 224, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btnControl.setObjectName("btnControl")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 30, 351, 41))
        self.label.setStyleSheet("color: rgb(11, 115, 40);\n"
"")
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(660, 540, 135, 30))
        self.pushButton_4.setMinimumSize(QtCore.QSize(50, 30))
        self.pushButton_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(133, 185, 224, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 340, 159, 30))
        self.pushButton.setMinimumSize(QtCore.QSize(50, 30))
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(133, 185, 224, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 340, 159, 30))
        self.pushButton_3.setMinimumSize(QtCore.QSize(50, 30))
        self.pushButton_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(133, 185, 224, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 540, 135, 30))
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 30))
        self.pushButton_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(133, 185, 224, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.open_files()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Контроль целостности"))
        self.groupBox.setTitle(_translate("MainWindow", "Действия с файлами"))
        self.btnDel.setText(_translate("MainWindow", "Удалить из списка"))
        self.btnChoose.setText(_translate("MainWindow", "Выбрать"))
        self.btnRecovery.setText(_translate("MainWindow", "Восстановить"))
        self.btnControl.setText(_translate("MainWindow", "Добавить на КЦ"))
        self.label.setText(_translate("MainWindow", "Следующие файлы добавлены на КЦ"))
        self.pushButton_4.setText(_translate("MainWindow", "ОК"))
        self.pushButton.setText(_translate("MainWindow", "Снять с КЦ"))
        self.pushButton_3.setText(_translate("MainWindow", "Проверить КЦ"))
        self.pushButton_2.setText(_translate("MainWindow", "Отмена"))

    #  Вызов функции для выбора файлов
    def open_files(self):
        self.btnChoose.clicked.connect(self.choose_files)

    def choose_files(self):
        res = QFileDialog.getOpenFileNames(None, 'Откройте файл', '/home/spi_729-1/Документы', 'txt file (*.txt);;jpg file (*.jpg)')
        print(res)
        dirname = QFileDialog.getExistingDirectory(None, 'Откройте папку', '/home/spi_729-1/Документы')
        print(dirname)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # create applicatio
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())  # execute the app