#
# main.py
# EverCal
#
# Created by Martin Cao on 2024/09/26.
#
import sys
import time

from PySide6.QtCore import Qt, QDate, QFile
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PySide6.QtUiTools import QUiLoader
from sqlalchemy.sql.functions import current_date

from view.EverCal import Ui_MainWindow
from view.monthView import Ui_monthView
from view.dateMonthView import Ui_Form as Ui_dateMonthView
from view.eventMonthView import Ui_Form as Ui_eventMonthView
from view_model.init import init_ui
from database.DatabaseConnection import *


class MainWindow(QMainWindow):
    def __init__(self, db_connection: DatabaseConnection):
        super(MainWindow, self).__init__()

        # Setup MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("EverCal") # Modify the window name to EverCal

        # Setup monthView
        self.monthView = QWidget()
        self.monthView_ui = Ui_monthView()
        self.monthView_ui.setupUi(self.monthView)

        # # Setup dateMonthView
        # self.dateMonthView = QWidget()
        # self.dateMonthView_ui = Ui_dateMonthView()
        # self.dateMonthView_ui.setupUi(self.dateMonthView)
        #
        # # Setup eventMonthView
        # self.eventMonthView = QWidget()
        # self.eventMonthView_ui = Ui_eventMonthView()
        # self.eventMonthView_ui.setupUi(self.eventMonthView)

        # # region ui test
        # # Add eventMonthView to dateMonthView's vertical layout
        # self.dateMonthView_ui.verticalLayout_dateMonthView.addWidget(self.eventMonthView)
        #
        # # Add dateMonthView to monthView's grid layout
        # self.monthView_ui.gridLayout_monthView_calendarGrid.addWidget(self.dateMonthView)

        # Add monthView to MainWindow's Month's grid layout
        self.ui.gridLayout_monthView.addWidget(self.monthView)
        # endregion

        # Auto layout
        self.setCentralWidget(self.ui.gridWidget)

        self.displayed_today: QDate = QDate.currentDate()
        self.displayed_year: int = self.displayed_today.year()
        self.displayed_month: int = self.displayed_today.month()
        self.displayed_day: int = self.displayed_today.day()

        def setupDay(day: QDate):
            self.displayed_today = day
            self.displayed_year = day.year()
            self.displayed_month = day.month()
            self.displayed_day = day.day()
            init_ui(self.monthView, self.displayed_year, self.displayed_month, default_start_day, db_connection)

        default_start_day: int = 0  # The week starts on Sunday

        # Initialize the month view
        init_ui(self.monthView, self.displayed_year, self.displayed_month, default_start_day, db_connection)

        self.button_previous_month = self.monthView.findChild(QPushButton, "pushButton_monthView_header_previous")
        self.button_next_month = self.monthView.findChild(QPushButton, "pushButton_monthView_header_next")
        self.button_today = self.monthView.findChild(QPushButton, "pushButton_monthView_header_today")

        self.button_today.clicked.connect(lambda: setupDay(QDate.currentDate()))
        self.button_previous_month.clicked.connect(lambda: setupDay(self.displayed_today.addMonths(-1)))
        self.button_next_month.clicked.connect(lambda: setupDay(self.displayed_today.addMonths(1)))

        # Set initial tab to month view
        self.ui.tabWidget.setCurrentIndex(2)


if __name__ == "__main__":

    app = QApplication([])

    # if sys.platform == "darwin": # macOS
    #     app.setStyle("macintosh")
    # elif sys.platform == "win32": # Windows
    #     app.setStyle("windowsvista")

    db_connection = DatabaseConnection()

    window = MainWindow(db_connection)
    window.show()
    app.exec()

