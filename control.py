# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1799, 888)
        MainWindow.setMinimumSize(QtCore.QSize(1799, 888))
        MainWindow.setMaximumSize(QtCore.QSize(1799, 888))
        MainWindow.setStyleSheet("background-color: rgb(56, 201, 233);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 380, 711, 161))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(188, 128, 233, 255), stop:1 rgba(255, 255, 255, 255));")
        self.groupBox.setObjectName("groupBox")
        self.btnDel = QtWidgets.QPushButton(self.groupBox)
        self.btnDel.setGeometry(QtCore.QRect(510, 40, 159, 40))
        self.btnDel.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnDel.setFont(font)
        self.btnDel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(133, 185, 224, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btnDel.setObjectName("btnDel")
        self.btnChoosefile = QtWidgets.QPushButton(self.groupBox)
        self.btnChoosefile.setGeometry(QtCore.QRect(30, 40, 159, 40))
        self.btnChoosefile.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnChoosefile.setFont(font)
        self.btnChoosefile.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(133, 185, 224, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btnChoosefile.setObjectName("btnChoosefile")
        self.btnControl = QtWidgets.QPushButton(self.groupBox)
        self.btnControl.setGeometry(QtCore.QRect(270, 110, 159, 40))
        self.btnControl.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnControl.setFont(font)
        self.btnControl.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(133, 185, 224, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btnControl.setObjectName("btnControl")
        self.btnChoosedir = QtWidgets.QPushButton(self.groupBox)
        self.btnChoosedir.setGeometry(QtCore.QRect(270, 40, 159, 40))
        self.btnChoosedir.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnChoosedir.setFont(font)
        self.btnChoosedir.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(133, 185, 224, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btnChoosedir.setObjectName("btnChoosedir")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1100, 10, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1420, 370, 221, 40))
        self.pushButton.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(133, 185, 224, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(920, 370, 159, 40))
        self.pushButton_3.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(133, 185, 224, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton_3.setObjectName("pushButton_3")
        self.listWidgetChoose = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetChoose.setGeometry(QtCore.QRect(30, 60, 711, 301))
        self.listWidgetChoose.setStyleSheet("background-color: rgb(213, 245, 249);")
        self.listWidgetChoose.setObjectName("listWidgetChoose")
        self.listWidgetControl = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetControl.setGeometry(QtCore.QRect(780, 60, 991, 301))
        self.listWidgetControl.setStyleSheet("\n"
"background-color: rgb(213, 245, 249);")
        self.listWidgetControl.setObjectName("listWidgetControl")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.listWidgetOutput = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetOutput.setGeometry(QtCore.QRect(780, 460, 991, 411))
        self.listWidgetOutput.setStyleSheet("background-color: rgb(213, 245, 249);")
        self.listWidgetOutput.setObjectName("listWidgetOutput")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1150, 410, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.label_3.setObjectName("label_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 560, 711, 311))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("background-color: rgb(225, 186, 241);\n"
"")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnRecovery = QtWidgets.QPushButton(self.groupBox_2)
        self.btnRecovery.setGeometry(QtCore.QRect(270, 260, 159, 40))
        self.btnRecovery.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnRecovery.setFont(font)
        self.btnRecovery.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(133, 185, 224, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btnRecovery.setObjectName("btnRecovery")
        self.textPathOut = QtWidgets.QTextEdit(self.groupBox_2)
        self.textPathOut.setGeometry(QtCore.QRect(10, 200, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.textPathOut.setFont(font)
        self.textPathOut.setReadOnly(True)
        self.textPathOut.setObjectName("textPathOut")
        self.btndir_backup = QtWidgets.QPushButton(self.groupBox_2)
        self.btndir_backup.setGeometry(QtCore.QRect(510, 240, 159, 40))
        self.btndir_backup.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btndir_backup.setFont(font)
        self.btndir_backup.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(133, 185, 224, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btndir_backup.setObjectName("btndir_backup")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 481, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.textPathIn = QtWidgets.QTextEdit(self.groupBox_2)
        self.textPathIn.setGeometry(QtCore.QRect(10, 90, 471, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.textPathIn.setFont(font)
        self.textPathIn.setReadOnly(True)
        self.textPathIn.setObjectName("textPathIn")
        self.btnChoosefile_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.btnChoosefile_2.setGeometry(QtCore.QRect(510, 90, 159, 40))
        self.btnChoosefile_2.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnChoosefile_2.setFont(font)
        self.btnChoosefile_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(133, 185, 224, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btnChoosefile_2.setObjectName("btnChoosefile_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(36, 31, 49);\n"
"")
        self.label_4.setObjectName("label_4")
        self.btnfile_backup = QtWidgets.QPushButton(self.groupBox_2)
        self.btnfile_backup.setGeometry(QtCore.QRect(510, 180, 159, 40))
        self.btnfile_backup.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.btnfile_backup.setFont(font)
        self.btnfile_backup.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(133, 185, 224, 255), stop:1 rgba(255, 255, 255, 255));")
        self.btnfile_backup.setObjectName("btnfile_backup")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Контроль целостности"))
        self.groupBox.setTitle(_translate("MainWindow", "Основные действия с файлами"))
        self.btnDel.setText(_translate("MainWindow", "Удалить из списка"))
        self.btnChoosefile.setText(_translate("MainWindow", "Выбрать файл"))
        self.btnControl.setText(_translate("MainWindow", "Добавить на КЦ"))
        self.btnChoosedir.setText(_translate("MainWindow", "Выбрать каталог"))
        self.label.setText(_translate("MainWindow", "           Следующие файлы добавлены на КЦ"))
        self.pushButton.setText(_translate("MainWindow", "Остановить проверку КЦ"))
        self.pushButton_3.setText(_translate("MainWindow", "Проверить КЦ"))
        self.label_2.setText(_translate("MainWindow", "Выбранные файлы для установки на КЦ"))
        self.label_3.setText(_translate("MainWindow", "Результат проверки КЦ файлов"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Восстановление файлов и каталогов"))
        self.btnRecovery.setText(_translate("MainWindow", "Восстановить"))
        self.btndir_backup.setText(_translate("MainWindow", "Каталог (backup)"))
        self.label_5.setText(_translate("MainWindow", "Каталог, в который нужно восстановить файл"))
        self.btnChoosefile_2.setText(_translate("MainWindow", "Выбрать каталог"))
        self.label_4.setText(_translate("MainWindow", "Путь к файлу для восстановления (Backup)"))
        self.btnfile_backup.setText(_translate("MainWindow", "Файл (backup)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
