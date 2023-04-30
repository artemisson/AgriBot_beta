from datetime import datetime, timedelta
from cal_setup import get_calendar_service
import datefinder
import datetime

start_time_str = ("2nd April 3 p.m.")
matches = list(datefinder.find_dates(start_time_str))
start_time_m = matches[0]
summary =str("Test Run1")

def create_event(start_time_m, summary,description=None, location=None):
    service = get_calendar_service()
    # Format the start time as AM/PM and print it
    ###
    start_time = start_time_m.strftime("%I:%M %p")
    end_time = start_time_m + timedelta(hours=2)
    event = {
        'summary' : summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_time_m.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Africa/Nairobi',
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
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
create_event(start_time_m, summary)