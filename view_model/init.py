from PySide6.QtWidgets import QWidget
from view_model.CalendarViewModel import CalendarViewModel

def init_ui(month_view: QWidget, year: int, month: int, start_day_of_week: int):
    """Initialize the interface with the given year and month."""
    calendar_view_model = CalendarViewModel(month_view)
    calendar_view_model.setup(year, month, start_day_of_week)