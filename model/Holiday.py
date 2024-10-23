from PySide6.QtCore import QDate
from lunarcalendar import Converter, Lunar

def get_china_holidays(year: int):
    holidays = {
        QDate(year, 1, 1): "元旦",
        QDate(year, 3, 8): "妇女节",
        QDate(year, 5, 1): "劳动节",
        QDate(year, 5, 4): "青年节",
        QDate(year, 6, 1): "儿童节",
        QDate(year, 7, 1): "建党节",
        QDate(year, 8, 1): "建军节",
        QDate(year, 10, 1): "国庆节",
    }

    # Lunar holidays
    lunar_holidays = {
        (1, 1): "春节",
        (2, 26): "清明节",
        (5, 5): "端午节",
        (8, 15): "中秋节",
    }

    # Ensure the year is within the valid range for the lunar calendar
    if not (1900 <= year <= 2100):
        raise ValueError(f"Year {year} is out of range for the lunar calendar")

    for (lunar_month, lunar_day), name in lunar_holidays.items():
        lunar_date = Converter.Lunar2Solar(Lunar(year, lunar_month, lunar_day))
        holidays[QDate(lunar_date.year, lunar_date.month, lunar_date.day)] = name

    return holidays