from typing import List, Optional
from PySide6.QtCore import QDate, QDateTime
from PySide6.QtGui import QColor
import uuid, time, hashlib
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()


class Event(Base):
    __tablename__ = 'events'
    event_id = Column(String, primary_key=True)
    name = Column(String)
    address = Column(String)
    calendar_id = Column(String, ForeignKey('calendars.id'))
    is_all_day = Column(Boolean)
    start_time = Column(String)
    end_time = Column(String)
    repeat_mode = Column(Integer)
    invitees = Column(String)
    notes = Column(String)
    url = Column(String)
    calendar = relationship("Calendar", back_populates="events")

    def __init__(self, name: str, address: str, calendar_id: str, is_all_day: bool,
                 start_time: QDateTime, end_time: QDateTime, invitees: List[str],
                 notes: str, url: str, repeat_mode: int = 0, event_id: Optional[int] = None):
        self.event_id: int = event_id if event_id is not None else uuid.uuid4()
        self.name: str = name
        self.address: str = address
        self.calendar_id: str = calendar_id
        self.is_all_day: bool = is_all_day
        self.start_time: QDateTime = start_time
        self.end_time: QDateTime = end_time
        self.repeat_mode: int = repeat_mode
        self.invitees: List[str] = invitees
        self.notes: str = notes
        self.url: str = url

class Calendar(Base):
    __tablename__ = 'calendars'
    id = Column(String, primary_key=True)
    name = Column(String)
    colour = Column(String)
    description = Column(String)
    created_at = Column(String)
    events = relationship("Event", back_populates="calendar")

    def __init__(self, name: str, colour: QColor = QColor.rgb(), description: str = "",
                 created_at: Optional[str] = None):
        self.events: List[Event] = []
        self.name: str = name
        self.colour: QColor = colour
        self.description: str = description
        self.created_at: str = created_at if created_at else str(int(time.time()))
        self.id: str = f"{name}_{hashlib.sha256(f'{name}{self.created_at}'.encode()).hexdigest()}" # id = name_{hash(name + created_at)}

    def add_event(self, event: Event) -> None:
        self.events.append(event)

    def get_events_for_date(self, date: QDate) -> List[Event]:
        events_on_date: List[Event] = []
        for event in self.events:
            if event.start_time.date() <= date <= event.end_time.date():
                events_on_date.append(event)
        return events_on_date

# region old class Event & Calendar declaration

# class Event:
#     def __init__(self, name: str, address: str, calendarId: str, isAllDay: bool,
#                  startTime: QDateTime, endTime: QDateTime, invitees: List[str],
#                  notes: str, url: str, repeatMode: int = 0, eventId: Optional[int] = None):
#         self.eventId: int = eventId if eventId is not None else uuid.uuid4()
#
#         self.name: str = name
#         self.address: str = address
#         self.calendarId: str = calendarId # belonged calendar
#         self.isAllDay: bool = isAllDay
#         self.startTime: QDateTime = startTime
#         self.endTime: QDateTime = endTime
#         self.repeatMode: int = repeatMode
#         """
#         repeatMode: int
#             0: none
#             1: every day
#             2: every week
#             3: every month
#             4: every year
#             5: custom
#         """
#         self.invitees: List[str] = invitees
#         self.notes: str = notes
#         self.url: str = url
#
#
# class Calendar:
#     def __init__(self, name: str, colour: QColor = QColor.rgb(), description: str = "",
#                  created_at: Optional[str] = None):
#         self.events: List[Event] = []
#         self.name: str = name
#         self.colour: QColor = colour
#         self.description: str = description
#         self.createdAt: str = created_at if created_at else str(int(time.time()))
#         self.id: str = f"{name}_{hashlib.sha256(f'{name}{self.createdAt}'.encode()).hexdigest()}"
#
#     def add_event(self, event: Event) -> None:
#         self.events.append(event)
#
#     def get_events_for_date(self, date: QDate) -> List[Event]:
#         eventsOnDate: List[Event] = []
#
#         for event in self.events:
#             if event.startTime.date() <= date <= event.endTime.date():
#                 eventsOnDate.append(event)
#
#         return eventsOnDate

# endregion
