import sys
from PyQt5.QtWidgets import *  # import section


class DlgMain(QDialog):
    # через self обращаемся к объектам класса, инициализируем констурктор
    def __init__(self):
        super().__init__()
        self.resize(200, 200)
        self.btn = QPushButton('Show message', self)
        self.btn.move(40, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        res = QMessageBox.question(self, 'MDisk full', 'Your disk drive is almost full')
        if res == QMessageBox.Yes:
            QMessageBox.information(self, '', "You have clicked 'Yes' btn")
        elif res == QMessageBox.No:
            QMessageBox.information(self, '', "You have clicked 'No' btn")


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
