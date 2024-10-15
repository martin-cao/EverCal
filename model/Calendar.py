from typing import List, Optional
from PySide6.QtCore import QDate
from PySide6.QtGui import QColor, Qt
import uuid, time, hashlib
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from model.Event import Event
from model.Base import Base

class Calendar(Base):
    __tablename__ = 'calendars'
    id = Column(String, primary_key=True)
    name = Column(String)
    colour = Column(String)
    description = Column(String)
    created_at = Column(String)
    events = relationship("Event", back_populates="calendar")

    def __init__(self, name: str, colour: QColor = QColor(Qt.GlobalColor.red), description: str = "",
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
            if event.occurs_on(date):
                events_on_date.append(event)
        return events_on_date