from datetime import datetime, time


class Attendence:
    def __init__(self, date: datetime):
        self.current_date = date
        self.ontime = False

    def is_on_time(self):
        morning_start: time = time(8, 0, 0)

        if self.current_date.time() <= morning_start:
            return 'ON TIME'
        else:
            return 'LATE'
