from typing import List
from PySide6.QtCore import QDate
from model.Calendar import Calendar, Event
from database.DatabaseConnection import DatabaseConnection


class CalendarModel:
    def __init__(self, db_connection: DatabaseConnection):
        self.session = db_connection.session

    def insert_calendar(self, calendar: Calendar):
        self.session.add(calendar)
        self.session.commit()
        return calendar.id

    def insert_event(self, event: Event):
        self.session.add(event)
        self.session.commit()

    def insert_repeated_events(self, event: Event, end_date: QDate):
        repeated_events = event.generate_repeated_events(end_date)
        for repeated_event in repeated_events:
            self.session.add(repeated_event)
        self.session.commit()

    def get_calendars(self) -> List[Calendar]:
        calendars = self.session.query(Calendar).all()
        return calendars

    def get_events(self, calendar_id: str) -> List[Event]:
        events = self.session.query(Event).filter_by(calendar_id=calendar_id).all()
        return events

    def get_events_for_date(self, date: QDate) -> List[Event]:
        events = self.session.query(Event).all()
        events_on_date = [
            event for event in events
            if event.start_time.date() <= date <= event.end_time.date() or event.is_all_day
        ]
        return events_on_date

    def get_repeated_events_around(self, event: Event, reference_date: QDate, count: int = 10) -> List[Event]:
        return event.generate_repeated_events_around(reference_date, count)

    def update_calendar(self, calendar: Calendar):
        existing_calendar = self.session.query(Calendar).filter_by(id=calendar.id).first()
        if existing_calendar:
            existing_calendar.name = calendar.name
            existing_calendar.colour = calendar.colour
            existing_calendar.description = calendar.description
            self.session.commit()

    def update_event(self, event: Event):
        existing_event = self.session.query(Event).filter_by(event_id=event.event_id).first()
        if existing_event:
            existing_event.name = event.name
            existing_event.address = event.address
            existing_event.calendar_id = event.calendar_id
            existing_event.is_all_day = event.is_all_day
            existing_event.start_time = event.start_time
            existing_event.end_time = event.end_time
            existing_event.repeat_rule = event.repeat_rule
            existing_event.invitees = event.invitees
            existing_event.notes = event.notes
            existing_event.url = event.url
            self.session.commit()

    def delete_calendar(self, calendar_id: str):
        self.session.query(Calendar).filter_by(id=calendar_id).delete()
        self.session.commit()

    def delete_event(self, event_id: str):
        self.session.query(Event).filter_by(event_id=event_id).delete()
        self.session.commit()

