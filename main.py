#
# main.py
# EverCal
#
# Created by Martin Cao on 2024/09/26.
#
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from view.EverCal import Ui_MainWindow
from view.monthView import Ui_monthView
from view.dateMonthView import Ui_Form as Ui_dateMonthView
from view.eventMonthView import Ui_Form as Ui_eventMonthView


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Setup MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("EverCal") # Modify the window name to EverCal

        # Setup monthView
        self.monthView = QWidget()
        self.monthView_ui = Ui_monthView()
        self.monthView_ui.setupUi(self.monthView)

        # Setup dateMonthView
        self.dateMonthView = QWidget()
        self.dateMonthView_ui = Ui_dateMonthView()
        self.dateMonthView_ui.setupUi(self.dateMonthView)

        # Setup eventMonthView
        self.eventMonthView = QWidget()
        self.eventMonthView_ui = Ui_eventMonthView()
        self.eventMonthView_ui.setupUi(self.eventMonthView)

        # Add eventMonthView to dateMonthView's vertical layout
        self.dateMonthView_ui.verticalLayout_dateMonthView.addWidget(self.eventMonthView)

        # Add dateMonthView to monthView's grid layout
        self.monthView_ui.gridLayout_monthView_calendarGrid.addWidget(self.dateMonthView)

        # Add monthView to MainWindow's Month's grid layout
        self.ui.gridLayout_monthView.addWidget(self.monthView)

        # Auto layout
        self.setCentralWidget(self.ui.gridWidget)

        # Bind widgets and slots
        self.bind()

    def bind(self):
        pass

if __name__ == '__main__':

    app = QApplication([])

    # if sys.platform == "darwin": # macOS
    #     app.setStyle("macintosh")
    # elif sys.platform == "win32": # Windows
    #     app.setStyle("windowsvista")

    window = MainWindow()
    window.show()
    app.exec()