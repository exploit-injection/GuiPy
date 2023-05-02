# import sys
# from PyQt5.QtWidgets import *  # import section
#
# app = QApplication(sys.argv)  # create application
# dlgMain = QMainWindow()  # create main GUI window
# dlgMain.setWindowTitle('First GUI')  # properties
# dlgMain.show()  # show the GUI
#
# sys.exit(app.exec_())  # execute the app

import sys
from PyQt5.QtWidgets import *  # import section


class DlgMain(QDialog):
    # через self обращаемся к объектам класса, инициализируем констурктор
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Second GUI')  # add widgets, set properties
        self.resize(300, 200)  # install size window
        self.ledText = QLineEdit('Hello!', self)  # add widgets
        self.ledText.move(85, 95)  # install position

        self.btnUpdate = QPushButton('Update Window Title', self)
        self.btnUpdate.move(75, 130)
        self.btnUpdate.clicked.connect(self.evt_btnupdate_clicked)  # if click btn Update

    def evt_btnupdate_clicked(self):
        self.setWindowTitle(self.ledText.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
