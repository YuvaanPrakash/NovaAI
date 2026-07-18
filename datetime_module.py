"""
datetime_module.py
Handles all date and time related operations.
"""

from datetime import datetime, date
import calendar


class DateTimeModule:

    def get_time(self):
        """Return current time."""
        return datetime.now().strftime("%I:%M:%S %p")

    def get_date(self):
        """Return today's date."""
        return date.today().strftime("%d %B %Y")

    def get_day(self):
        """Return today's day."""
        return datetime.now().strftime("%A")

    def get_month(self):
        """Return current month."""
        return datetime.now().strftime("%B")

    def get_year(self):
        """Return current year."""
        return datetime.now().strftime("%Y")

    def get_calendar(self):
        """Return calendar of current month."""
        now = datetime.now()
        return calendar.month(now.year, now.month)

    def days_between(self, year, month, day):
        """
        Calculate number of days from today to a given date.
        """
        try:
            target = date(year, month, day)
            today = date.today()

            difference = target - today

            if difference.days > 0:
                return f"{difference.days} day(s) remaining."

            elif difference.days < 0:
                return f"{abs(difference.days)} day(s) ago."

            else:
                return "That's today!"

        except ValueError:
            return "Invalid date."

    def execute(self, command):

        command = command.lower().strip()

        if command == "time":
            return self.get_time()

        elif command == "date":
            return self.get_date()

        elif command == "day":
            return self.get_day()

        elif command == "month":
            return self.get_month()

        elif command == "year":
            return self.get_year()

        elif command == "calendar":
            return self.get_calendar()

        else:
            return "Unknown date/time command."


datetime_module = DateTimeModule()


if __name__ == "__main__":

    while True:

        cmd = input("DateTime > ")

        if cmd == "exit":
            break

        elif cmd == "days":
            y = int(input("Year : "))
            m = int(input("Month: "))
            d = int(input("Day  : "))
            print(datetime_module.days_between(y, m, d))

        else:
            print(datetime_module.execute(cmd))