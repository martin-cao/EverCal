from PySide6.QtWidgets import QWidget, QGridLayout, QFrame, QSizePolicy, QLabel, QVBoxLayout, QSpacerItem, \
    QItemEditorCreatorBase
from PySide6.QtCore import QDate, Qt
from model.Event import Event
# from view.dateMonthView import Ui_Form as Ui_dateMonthView
from view.dateMonthView_custom import CustomDateMonthView as Ui_dateMonthView
from view.eventMonthView import Ui_Form as Ui_eventMonthView
from view_model.EventMonthViewModel import EventMonthViewModel
from database.models import CalendarModel as db, CalendarModel
from database.DatabaseConnection import *
from model.Calendar import *


class DateMonthViewModel:
    def __init__(self, view: QWidget, vertical_layout: QVBoxLayout, db_connection: DatabaseConnection):
        self.date_view = view

        for child in self.date_view.children():
            print(f"{child.objectName()}, {type(child).__name__}")

        self.vertical_layout = vertical_layout

        if self.vertical_layout is None:
            raise ValueError("Vertical layout 'verticalLayout_dateMonthView' not found in the view")

        self.db = db_connection.session.query(Calendar).first()

        if self.db is None:
            raise ValueError("No Calendar object found in the database")

    def setup_dateView(self, date: QDate):
        # Get all events on the date
        events: [Event] = self.db.get_events_for_date(date)

        # Clear existing items in the vertical layout
        while self.vertical_layout.count():
            item = self.vertical_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # Add events to the vertical layout
        for event in events:
            event_view = QWidget()
            event_view_ui = Ui_eventMonthView()
            event_view_ui.setupUi(event_view)

            colour_label = event_view.findChild(QLabel, "label_eventMonthView_calendarLabel")
            colour_label.setStyleSheet(f"background-color: {event.calendar.colour.name()}; border-radius: 2px;")
            event_label = event_view.findChild(QLabel, "label_eventMonthView_eventTitle")
            event_label.setText(event.name)
            time_label = event_view.findChild(QLabel, "label_eventMonthView_time")
            time_label.setText(event.start_time.toString("hh:mm AP"))

            self.vertical_layout.addWidget(event_view)

        # Add a vertical spacer at the bottom
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.vertical_layout.addItem(spacer)




