import sys
from PyQt5.QtWidgets import *  # import section


class DlgMain(QDialog):
    # через self обращаемся к объектам класса, инициализируем констурктор
    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton('Age btn', self)
        self.btn.move(40, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

        self.btn2 = QPushButton('Colors btn', self)
        self.btn2.move(40, 80)
        self.btn2.clicked.connect(self.evt_btn2_clicked)

    def evt_btn_clicked(self):
        i_age, b_Ok = QInputDialog.getInt(self, 'Title', 'Enter your age', 18, 18, 65, 1)
        if b_Ok:
            QMessageBox.information(self, 'Age', 'Your age is ' + str(i_age))
        else:
            QMessageBox.information(self, 'Canceled', 'User have clicked `Cancel`')

    def evt_btn2_clicked(self):
        colors = ['red', 'green', 'yellow', 'blue', 'orange']
        s_color, b_Ok2 = QInputDialog.getItem(self, 'Title', 'Enter your favorite color', colors, editable=False)

        if b_Ok2:
            QMessageBox.information(self, 'Color', 'Your favorite color is ' + s_color)
        else:
            QMessageBox.information(self, 'Canceled', 'User have clicked `Cancel` ')


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
