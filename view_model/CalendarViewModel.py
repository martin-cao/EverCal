from PySide6.QtCore import QDate, Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QFrame, QSizePolicy, QLabel
from view.dateMonthView import Ui_Form as Ui_dateMonthView

class CalendarViewModel:
    def __init__(self, month_view: QWidget):
        self.month_view = month_view
        self.grid_layout = month_view.findChild(QGridLayout, "gridLayout_monthView_calendarGrid")

    def setup(self, year: int, month: int, start_day_of_week: int):
        # Clear existing items in the grid layout
        while self.grid_layout.count():
            item = self.grid_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # Update the labels for the days of the week
        day_labels = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for i in range(7):
            label = self.month_view.findChild(QLabel, f"label_monthView_day_{i}")
            if label is not None:
                label.setText(day_labels[(start_day_of_week + i) % 7])
            else:
                print(f"Label label_monthView_day_{i} not found")

        # Get the first day of the month
        first_day = QDate(year, month, 1)
        # Get the day of the week for the first day (1 = Monday, 7 = Sunday)
        first_day_of_week = (first_day.dayOfWeek() + 6) % 7  # Convert to 0 = Sunday, 6 = Saturday
        start_day_of_week = (start_day_of_week + 6) % 7  # Convert to 0 = Sunday, 6 = Saturday
        offset = (first_day_of_week - start_day_of_week + 7) % 7

        # Get the number of days in the month
        days_in_month = first_day.daysInMonth()

        # Create date views for each day in the 7x6 grid
        day = 1
        for row in range(6):
            for col in range(7):
                date_view = QFrame()
                date_view.setFrameShape(QFrame.Box)
                date_view.setLineWidth(1)
                date_view_ui = Ui_dateMonthView()
                date_view_ui.setupUi(date_view)

                date_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                date_view.setContentsMargins(0, 0, 0, 0)

                date_view.setFrameShape(QFrame.Box)
                date_view.setLineWidth(2)
                date_view.setMidLineWidth(1)

                date_view_ui.label_dateMonthView_date.setAlignment(Qt.AlignRight | Qt.AlignTop)

                # Calculate the current date
                current_date = QDate(year, month, day)
                if row == 0 and col < offset: # Days before the first day of the month
                    previous_month_date = first_day.addMonths(-1).addDays(col - offset + 1)
                    if previous_month_date.day() == 1:
                        date_view_ui.label_dateMonthView_date.setText(previous_month_date.toString("MMM d"))
                    else:
                        date_view_ui.label_dateMonthView_date.setText(str(previous_month_date.day()))
                    date_view_ui.label_dateMonthView_date.setStyleSheet("color: gray;")
                elif day > days_in_month: # Days after the last day of the month
                    next_month_date = first_day.addMonths(1).addDays(day - days_in_month - 1)
                    if next_month_date.day() == 1:
                        date_view_ui.label_dateMonthView_date.setText(next_month_date.toString("MMM d"))
                    else:
                        date_view_ui.label_dateMonthView_date.setText(str(next_month_date.day()))
                    date_view_ui.label_dateMonthView_date.setStyleSheet("color: gray;")
                    day += 1
                else: # Valid days in the month
                    if day == 1:
                        date_view_ui.label_dateMonthView_date.setText(current_date.toString("MMM d"))
                    else:
                        date_view_ui.label_dateMonthView_date.setText(str(day))
                    day += 1

                self.grid_layout.addWidget(date_view, row, col)