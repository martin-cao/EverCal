from PySide6.QtWidgets import QWidget
from view_model.CalendarMonthViewModel import CalendarMonthViewModel
from database.DatabaseConnection import DatabaseConnection

def init_ui(view: QWidget, year: int, month: int, start_day_of_week: int, db_connection: DatabaseConnection):
    """Initialize the interface with the given year and month."""
    calendar_monthView_view_model = CalendarMonthViewModel(view, db_connection)
    calendar_monthView_view_model.setup_monthView(year, month, start_day_of_week)