from PyQt6.QtWidgets import QWidget, QGridLayout, QFrame, QSizePolicy, QLabel, QVBoxLayout, QSpacerItem, \
    QItemEditorCreatorBase
from PySide6.QtCore import QDate, Qt
from model.Event import Event
from view.dateMonthView import Ui_Form as Ui_dateMonthView
from view.eventMonthView import Ui_Form as Ui_eventMonthView
from view_model.EventMonthViewModel import EventMonthViewModel
from database.models import CalendarModel as db, CalendarModel
from database.DatabaseConnection import *
from model.Calendar import *


class DateMonthViewModel:
    def __init__(self, view: QWidget, db_connection: DatabaseConnection):
        self.date_view = view

        for child in self.date_view.children():
            print(f"{child.objectName()}, {type(child).__name__}")

        self.grid_layout = self.date_view.findChild(QGridLayout, "gridLayout")

        if self.grid_layout:
            print("gridLayout found")
            for i in range(self.grid_layout.count()):
                item = self.grid_layout.itemAt(i)
                widget = item.widget()  # 尝试获取布局中的小部件
                layout = item.layout()  # 尝试获取布局中的布局
                if widget:
                    print(f"Found widget: {widget.objectName()}")
                if layout:
                    print(f"Found layout: {layout.objectName()}")
                    if isinstance(layout, QVBoxLayout) and layout.objectName() == "verticalLayout_dateMonthView":
                        self.vertical_layout = layout
                        break



        if self.vertical_layout is None:
            raise ValueError("Vertical layout 'verticalLayout_dateMonthView' not found in the view")
        self.db = db_connection.session.query(Calendar).first()

    def setup_dateView(self, date: QDate):
        # Get all events on the date
        events: [Event] = self.db.get_events_for_date(date)

        # Clear existing items in the vertical layout
        while self.vertical_layout.count():
            item = self.vertical_layout.takeAt(0)
            if item.widget():
                item.widget.deleteLater()

        # Get the height of the dateMonthView
        available_height = self.date_view.height()

        # Calculate the height of a single event widget
        temp_event_view = QWidget()
        temp_event_view_ui = Ui_eventMonthView()
        temp_event_view_ui.setupUi(temp_event_view)
        event_height = temp_event_view.sizeHint().height()

        # Calculate the height of the QLabel for remaining events
        label_height = QLabel().sizeHint().height()

        # Add events to the vertical layout
        total_height = 0
        max_visible_events = 0
        for event in events:
            if total_height + event_height + label_height > available_height:
                break
            event_view = QWidget()
            event_view_ui = Ui_eventMonthView()
            event_view_ui.setupUi(event_view)
            event_view_model = EventMonthViewModel(event_view)
            event_view_model.setup_eventView(event)
            self.vertical_layout.addWidget(event_view)
            total_height += event_height
            max_visible_events += 1

        # Add a QLabel indicating how many more events are not displayed
        if max_visible_events < len(events):
            more_label = QLabel(f"+{len(events) - max_visible_events} more")
            more_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            self.vertical_layout.addWidget(more_label)

        # Add a vertical spacer at the bottom
        spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.vertical_layout.addItem(spacer)



