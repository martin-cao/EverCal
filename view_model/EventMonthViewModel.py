from PyQt6.QtWidgets import QWidget, QGridLayout, QFrame, QSizePolicy, QLabel
from PySide6.QtCore import QDate, Qt
from view.eventMonthView import Ui_Form as Ui_eventMonthView
from model.Event import Event


class EventMonthViewModel:
    def __init__(self, view: QWidget):
        self.event_view = view
        self.label_event_title = view.findChild(QLabel, "label_eventMonthView_eventTitle")
        self.label_event_time = view.findChild(QLabel, "label_eventMonthView_time")
        self.label_calendar_label = view.findChild(QLabel, "label_eventMonthView_calendarLabel")

    def setup_eventView(self, event: Event):
        self.label_event_title.setText(event.name)
        self.label_event_time.setText(event.time.toString("hh:mm AP"))
        calendar_colour = event.calendar.colour.name()
        self.label_calendar_label.setStyleSheet(f"background-color: {calendar_colour}; border-radius: 2px;")


