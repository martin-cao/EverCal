import json
from typing import List, Optional
from PySide6.QtCore import QDate, Qt

class RepeatRule:
    def __init__(self, mode: int, interval: int = 1, days_of_week: Optional[List[int]] = None,
                 day_of_month: Optional[int] = None, week_of_month: Optional[int] = None,
                 month_of_year: Optional[int] = None, is_infinite: bool = False, end_date: Optional[QDate] = None):
        self.mode = mode
        self.interval = interval
        self.days_of_week = days_of_week
        self.day_of_month = day_of_month
        self.week_of_month = week_of_month
        self.month_of_year = month_of_year
        self.is_infinite = is_infinite
        self.end_date = end_date

    def occurs_on(self, date: QDate, start_date: QDate) -> bool:
        if not (0 <= self.mode <= 5):
            raise ValueError(f"Invalid mode: {self.mode}. Mode must be between 0 and 5.")
        if self.end_date and date > self.end_date:
            return False
        if date < start_date:
            return False

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
                return False

    def generate_dates(self, start_date: QDate, reference_date: QDate, count: int = 10) -> List[QDate]:
        dates = []
        current_date = start_date
        while len(dates) < count:
            if self.occurs_on(current_date, start_date):
                dates.append(current_date)
            current_date = current_date.addDays(self.interval)
            if self.end_date and current_date > self.end_date:
                break
        return dates

    def to_json(self) -> str:
        data = self.__dict__.copy()
        if self.end_date:
            data['end_date'] = self.end_date.toString(Qt.ISODate)
        return json.dumps(data)

    @staticmethod
    def from_json(json_str: str) -> 'RepeatRule':
        print(f"Decoding JSON: {json_str}")  # Debugging statement
        data = json.loads(json_str)
        if 'end_date' in data and data['end_date']:
            data['end_date'] = QDate.fromString(data['end_date'], Qt.ISODate)
        return RepeatRule(**data)