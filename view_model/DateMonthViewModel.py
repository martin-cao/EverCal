from PySide6.QtWidgets import QWidget, QGridLayout, QFrame, QSizePolicy, QLabel, QVBoxLayout, QSpacerItem, \
    QItemEditorCreatorBase
from PySide6.QtCore import QDate, Qt, QDateTime, QTime
from model.Event import Event, HolidayType
from model.Holiday import get_china_holidays
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

        # debug
        # for child in self.date_view.children():
        #     print(f"{child.objectName()}, {type(child).__name__}")

        self.vertical_layout = vertical_layout

        # debug
        # if self.vertical_layout is None:
        #     raise ValueError("Vertical layout 'verticalLayout_dateMonthView' not found in the view")

        self.db = db_connection.session.query(Calendar).first()

        # debug
        # if self.db is None:
        #     raise ValueError("No Calendar object found in the database")

        self.holidays = get_china_holidays(QDate.currentDate().year())

    def setup_dateView(self, date: QDate, current_month):
        # Get all events on the date
        events: [Event] = self.db.get_events_for_date(date)
        self.holidays = get_china_holidays(date.year())

        # Ensure the year is within the valid range before calling get_china_holidays
        if 1900 <= date.year() <= 2100:
            self.holidays = get_china_holidays(date.year())
        else:
            self.holidays = {}

        if date in self.holidays:
            holiday_event = Event(
                name=self.holidays[date],
                address="",
                calendar_id="holiday_calendar",
                is_all_day=True,
                start_time=QDateTime(date, QTime(0, 0)),
                end_time=QDateTime(date, QTime(23, 59)),
                invitees=[],
                notes="",
                url="",
                holiday_type=HolidayType.GREGORIAN.value
            )
            events.append(holiday_event)

        # Check if the current day is part of the previous month
        # if date.month() < current_month:
        #     # Do not include events from the first day of the current month
        #     events = [event for event in events if event.startTime().date().month() != current_month]

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
            if event.calendar:
                colour_label.setStyleSheet(f"background-color: {event.calendar.colour.name()}; border-radius: 2px;")
            else:
                colour_label.setStyleSheet("background-color: gray; border-radius: 2px;")
            event_label = event_view.findChild(QLabel, "label_eventMonthView_eventTitle")
            event_label.setText(event.name)
            time_label = event_view.findChild(QLabel, "label_eventMonthView_time")
            time_label.setText("All Day" if event.is_all_day else event.start_time.toString("hh:mm AP"))

            self.vertical_layout.addWidget(event_view)

        # Add a vertical spacer at the bottom
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.vertical_layout.addItem(spacer)




