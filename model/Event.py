from typing import List, Optional
import uuid
from enum import Enum
from lunarcalendar import Converter, Lunar, Solar
from PySide6.QtCore import QDate, QDateTime, Qt
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
from model.Base import Base
from model.RepeatRule import RepeatRule


class HolidayType(Enum):
    NONE = 0
    GREGORIAN = 1
    LUNAR = 2

def generate_event_id() -> str:
    return str(uuid.uuid4())


class Event(Base):
    __tablename__ = 'events'
    event_id = Column(String, primary_key=True)
    name = Column(String)
    address = Column(String)
    calendar_id = Column(String, ForeignKey('calendars.id'))
    is_all_day = Column(Boolean)
    _start_time = Column("start_time", String)
    _end_time = Column("end_time", String)
    _repeat_rule = Column("repeat_rule", String)
    invitees = Column(String)
    notes = Column(String)
    url = Column(String)
    holiday_type = Column(Integer)
    calendar = relationship("Calendar", back_populates="events")

    def __init__(self, name: str, address: str, calendar_id: str, is_all_day: bool,
                 start_time: QDateTime, end_time: QDateTime, invitees: List[str],
                 notes: str, url: str, holiday_type: int = HolidayType.NONE.value, repeat_rule: Optional[RepeatRule] = None, event_id: Optional[int] = None):
        self.event_id: int = event_id if event_id is not None else generate_event_id()
        self.name: str = name
        self.address: str = address
        self.calendar_id: str = calendar_id
        self.is_all_day: bool = is_all_day
        self.start_time: QDateTime = start_time
        self.end_time: QDateTime = end_time
        self.repeat_rule: Optional[RepeatRule] = repeat_rule
        self.invitees: List[str] = invitees
        self.notes: str = notes
        self.url: str = url
        self.holiday_type: int = holiday_type

    @hybrid_property
    def start_time(self):
        return QDateTime.fromString(self._start_time, Qt.ISODate)

    @start_time.setter
    def start_time(self, value: QDateTime):
        self._start_time = value.toString(Qt.ISODate)

    @hybrid_property
    def end_time(self):
        return QDateTime.fromString(self._end_time, Qt.ISODate)

    @end_time.setter
    def end_time(self, value: QDateTime):
        self._end_time = value.toString(Qt.ISODate)

    @hybrid_property
    def repeat_rule(self):
        return RepeatRule.from_json(self._repeat_rule) if self._repeat_rule else None

    @repeat_rule.setter
    def repeat_rule(self, value: Optional[RepeatRule]):
        self._repeat_rule = value.to_json() if value else None

    def occurs_on(self, date: QDate) -> bool:
        if self.repeat_rule:
            return self.repeat_rule.occurs_on(date, self.start_time.date())
        return self.start_time.date() <= date <= self.end_time.date()

    def convert_solar_to_lunar(self, date: QDate) -> QDate:
        solar = Solar(date.year(), date.month(), date.day())
        lunar = Converter.Solar2Lunar(solar)
        return QDate(lunar.year, lunar.month, lunar.day)

    def convert_lunar_to_solar(lunar_year: int, lunar_month: int, lunar_day: int) -> QDate:
        lunar = Lunar(lunar_year, lunar_month, lunar_day)
        solar = Converter.LunarToSolar(lunar)
        return QDate(solar.year, solar.month, solar.day)

    def generate_repeated_events_around(self, reference_date: QDate, count: int = 10) -> List['Event']:
        if not self.repeat_rule:
            return [self]
        dates = self.repeat_rule.generate_dates(self.start_time.date(), reference_date, count)
        events = []
        for date in dates:
            new_event = Event(
                name=self.name,
                address=self.address,
                calendar_id=self.calendar_id,
                is_all_day=self.is_all_day,
                start_time=QDateTime(date, self.start_time.time()),
                end_time=QDateTime(date, self.end_time.time()),
                invitees=self.invitees,
                notes=self.notes,
                url=self.url,
                holiday_type=self.holiday_type,
                repeat_rule=self.repeat_rule,
                event_id=generate_event_id()
            )
            events.append(new_event)
        return events