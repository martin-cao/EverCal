from typing import List, Optional
from PySide6.QtCore import QDate

class RepeatRule:
    def __init__(self, mode: int, interval: int = 1, days_of_week: Optional[List[int]] = None,
                 day_of_month: Optional[int] = None, week_of_month: Optional[int] = None,
                 month_of_year: Optional[int] = None, is_infinite: bool = False):
        self.mode = mode
        self.interval = interval
        self.days_of_week = days_of_week
        self.day_of_month = day_of_month
        self.week_of_month = week_of_month
        self.month_of_year = month_of_year
        self.is_infinite = is_infinite

    def __repr__(self):
        return (f"RepeatRule(mode={self.mode}, interval={self.interval}, days_of_week={self.days_of_week}, "
                f"day_of_month={self.day_of_month}, week_of_month={self.week_of_month}, "
                f"month_of_year={self.month_of_year})")

    def occurs_on(self, date: QDate) -> bool:
        # Raise an error if self.mode is invalid
        if not (0 <= self.mode <= 5):
            raise ValueError(f"Invalid mode: {self.mode}. Mode must be between 0 and 5.")

        # Implement logic to check if the event occurs on the given date based on the repeat rule
        match self.mode:
            case 0:  # None
                return False
            case 1:  # Daily
                return True
            case 2:  # Weekly
                return date.dayOfWeek() in self.days_of_week
            case 3:  # Monthly
                return date.day() == self.day_of_month
            case 4:  # Yearly
                return date.month() == self.month_of_year and date.day() == self.day_of_month
            case _:
                # Add more logic for custom modes if needed
                return False

    def generate_dates(self, start_date: QDate, reference_date: QDate, count: int = 10) -> List[QDate]:
        dates = []
        current_date = start_date
        while len(dates) < count:
            if self.occurs_on(current_date):
                dates.append(current_date)
            current_date = current_date.addDays(self.interval)
        return dates