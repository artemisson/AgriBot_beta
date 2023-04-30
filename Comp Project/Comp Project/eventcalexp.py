from datetime import datetime, timedelta
from cal_setup import get_calendar_service
import datefinder
import datetime


def convert_time(start_time):
    time_obj = datetime.datetime.strptime(start_time, "%I:%M %p")
    return time_obj.time()


start_time_str = ("25th March 9PM")
summary =str("Test Run1")


def create_event(start_time_str, summary, duration=2, description=None, location=None):
    service = get_calendar_service()
    start_time_str =("25th march 10am")
    matches = list(datefinder.find_dates(start_time_str))
    start_time_m = matches[0]
    # Format the start time as AM/PM and print it
    start_time = start_time_m.strftime("%I:%M %p")
    start_time_ = convert_time(start_time)
    end_time_ = (datetime.datetime.combine(datetime.date.today(), start_time_) + datetime.timedelta(hours=2)).time()
    # Create the event dictionary with the specified details
    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_time_.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Africa/Nairobi',
        },
        'end': {
            'dateTime': end_time_.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Africa/Nairobi',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24*60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }
    return service.events().insert(calendarId ='primary', body=event).execute()
create_event(start_time_, summary)