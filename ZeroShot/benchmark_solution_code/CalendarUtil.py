'''
# This is a class as CalendarUtil that provides functionalities to manage calendar events, schedule appointments, and perform conflict checks.

from datetime import datetime, timedelta

class CalendarUtil:
    def __init__(self):
        """
        Initialize the calendar with an empty list of events.

    def add_event(self, event):
        """
        Add an event to the calendar.
        """

    def remove_event(self, event):
        """
        Remove an event from the calendar.
        """

    def get_events(self, date):
        """
        Get all events on a given date.
        """

    def is_available(self, start_time, end_time):
        """
        Check if the calendar is available for a given time slot.
        :return: True if the calendar is available for the given time slot, False otherwise,bool.
        """

    def get_available_slots(self, date):
        """
        Get all available time slots on a given date.
        :return: A list of available time slots on the given date,list.
        """

    def get_upcoming_events(self, num_events):
        """
        Get the next n upcoming events from a given date.
        :return: A list of the next n upcoming events from the given date,list.
        """

'''

from datetime import datetime, timedelta

class CalendarUtil:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def remove_event(self, event):
        if event in self.events:
            self.events.remove(event)

    def get_events(self, date):
        events_on_date = []
        for event in self.events:
            if event['date'].date() == date.date():
                events_on_date.append(event)
        return events_on_date

    def is_available(self, start_time, end_time):
        for event in self.events:
            if start_time < event['end_time'] and end_time > event['start_time']:
                return False
        return True

    def get_available_slots(self, date):
        available_slots = []
        start_time = datetime(date.year, date.month, date.day, 0, 0)
        end_time = datetime(date.year, date.month, date.day, 23, 59)

        while start_time < end_time:
            slot_end_time = start_time + timedelta(minutes=60)
            if self.is_available(start_time, slot_end_time):
                available_slots.append((start_time, slot_end_time))
            start_time += timedelta(minutes=60)


        return available_slots

    def get_upcoming_events(self, num_events):
        now = datetime.now()
        upcoming_events = []
        for event in self.events:
            if event['start_time'] >= now:
                upcoming_events.append(event)
            if len(upcoming_events) == num_events:
                break
        return upcoming_events