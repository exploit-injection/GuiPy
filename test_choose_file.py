import sys
from PyQt5.QtWidgets import *  # import section


class DlgMain(QDialog):
    # через self обращаемся к объектам класса, инициализируем констурктор
    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton('Open File', self)
        self.btn.move(40, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

        self.btn = QPushButton('Open Files', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.evt_btn2_clicked)

    # Choose one file (known directory)
    def evt_btn_clicked(self):
        res = QFileDialog.getOpenFileName(self, 'Open File', '/home/spi_729-1/Документы', 'txt file (*.txt);;jpg file (*.jpg)')
        print(res)

    # Choose more one file (start directory)
    def evt_btn2_clicked(self):
        res = QFileDialog.getOpenFileNames(self, 'Open File', '/home', 'txt file (*.txt);;jpg file (*.jpg)')
        print(res)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()  # show GUI
    sys.exit(app.exec_())  # execute the application
