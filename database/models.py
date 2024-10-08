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
            existing_event.repeat_mode = event.repeat_mode
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


# region old class CalendarModel declaration

# class CalendarModel:
#     def __init__(self, db_connection: DatabaseConnection):
#         self.connection = db_connection.connection
#         self.cursor = db_connection.cursor
#         self.create_tables()
#
#     def create_tables(self):
#         self.cursor.execute("""CREATE TABLE IF NOT EXISTS calendars (
#                                 id TEXT PRIMARY KEY,
#                                 name TEXT,
#                                 colour TEXT,
#                                 description TEXT,
#                                 createdAt TEXT)""")
#         self.cursor.execute("""CREATE TABLE IF NOT EXISTS events (
#                                 eventId TEXT PRIMARY KEY,
#                                 name TEXT,
#                                 address TEXT,
#                                 calendarId TEXT,
#                                 isAllDay BOOLEAN,
#                                 startTime TEXT,
#                                 endTime TEXT,
#                                 repeatMode INTEGER,
#                                 invitees TEXT,
#                                 notes TEXT,
#                                 url TEXT,
#                                 FOREIGN KEY(calendarId) REFERENCES calendars(id))""")
#         self.connection.commit()
#
#     def insert_calendar(self, calendar: Calendar):
#         self.cursor.execute("""INSERT INTO calendars (id, name, colour, description, createdAt)
#                                VALUES (?, ?, ?, ?, ?)""",
#                             (calendar.id, calendar.name, calendar.colour.name(), calendar.description, calendar.created_at))
#         self.connection.commit()
#         return calendar.id
#
#     def insert_event(self, event: Event):
#         self.cursor.execute("""INSERT INTO events (eventId, name, address, calendarId, isAllDay, startTime, endTime, repeatMode, invitees, notes, url)
#                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
#                             (str(event.event_id), event.name, event.address, event.calendar_id, event.is_all_day,
#                              event.start_time.toString(), event.end_time.toString(), event.repeat_mode,
#                              ",".join(event.invitees), event.notes, event.url))
#         self.connection.commit()
#
#     def get_calendars(self) -> List[Calendar]:
#         self.cursor.execute("SELECT id, name, colour, description, created_at FROM calendars")
#         rows = self.cursor.fetchall()
#         return [Calendar(name=row[1], colour=QColor(row[2]), description=row[3], created_at=row[4]) for row in rows]
#
#     def get_events(self, calendarId: str) -> List[Event]:
#         self.cursor.execute(
#             "SELECT eventId, name, address, calendarId, isAllDay, startTime, endTime, repeatMode, invitees, notes, url FROM events WHERE calendarId = ?",
#             (calendarId,))
#         rows = self.cursor.fetchall()
#         return [Event(event_id=row[0], name=row[1], address=row[2], calendar_id=row[3], is_all_day=row[4],
#                       start_time=QDateTime.fromString(row[5]), end_time=QDateTime.fromString(row[6]), repeat_mode=row[7],
#                       invitees=row[8].split(","), notes=row[9], url=row[10]) for row in rows]

# endregion