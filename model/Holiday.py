from PySide6.QtCore import QDate
from lunarcalendar import Converter, Lunar

def get_china_holidays(year: int):
    holidays = {
        QDate(year, 1, 1): "元旦",
        QDate(year, 5, 1): "劳动节",
        QDate(year, 10, 1): "国庆节",
    }

    # Lunar holidays
    lunar_holidays = {
        (1, 1): "春节",
        (5, 5): "端午节",
        (8, 15): "中秋节",
    }

    for (lunar_month, lunar_day), name in lunar_holidays.items():
        lunar_date = Converter.Lunar2Solar(Lunar(year, lunar_month, lunar_day))
        holidays[QDate(lunar_date.year, lunar_date.month, lunar_date.day)] = name

    return holidays