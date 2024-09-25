from PySide6.QtWidgets import QApplication, QMainWindow
from EverCal import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.bind()

    def bind(self):
        self.ui.pushButton.clicked.connect(lambda : print("Hello World!"))

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()