# EverCal

> [!NOTE]
> This is an assignment design for **2024 Fall** _Python Programming_ by student ID: `547a1ec97aff5d1cc4d5c510fcd126a8` (MD5 Hash).

**EverCal** is a custom-built calendar application designed to support daily, weekly, monthly, and yearly views of events. It is developed using Python and PySide6, providing an intuitive graphical interface for users to manage events, holidays, and other time-based information. It supports features like recurring events, all-day events, and integrates with external libraries to handle lunar dates for Chinese holidays.

## Features
- **Yearly, Monthly, Weekly, and Daily Views**: View events in different layouts.
- **All-Day Events**: Display full-day events in a simplified format.
- **Recurring Events**: Create events that repeat daily, weekly, monthly, yearly, or customize your own repeating pattern.
- **Lunar Calendar Support**: Integrates the lunarcalendar library to support Chinese holidays based on lunar dates.
- **Custom Events**: Add events with detailed information including name, time, location, invitees, and notes.
- **SQLite Integration**: Events are stored in an SQLite database for persistence across sessions.
- **Holiday Display**: Pre-configured Chinese mainland holidays (e.g., National Day, Spring Festival) are displayed annually without database storage.

## Getting Started

### Prerequisites
- `Python 3.11`
- `PySide6`
- `sqlalchemy`
- `lunarcalendar`

### Installation
1. Clone the repository:
``` shell
git clone https://github.com/martin-cao/EverCal.git
cd EverCal
```

2. Install the required packages:
```shell
pip install -r requirements.txt
```

3. Run the app:
```shell
python main.py
```

## Roadmap
- [ ] Daily, Weekly & Yearly view
- [ ] Add, Edit & Delete events
- [ ] Timezone Support
- [ ] Independent All-Day Event UI
- [ ] iCalendar Support
- [ ] CLI Calendar Management

> [!WARNING]
> As this is an assignment project, please **DO NOT pull request!** If you have any suggestion about this project, please create an issue.

For more information, please contact <a href="mailto:martincao119@icloud.com">martincao119@icloud.com</a>.
