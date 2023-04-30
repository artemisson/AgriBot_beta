from datetime import datetime, timedelta
from cal_setup import get_calendar_service
import datefinder
import datetime

def convert_time(start_time):
    time_obj = datetime.datetime.strptime(start_time, "%I:%M %p")
    return time_obj.time()

def main():
   # creates one hour event tomorrow 10 AM IST
    service = get_calendar_service()
    start_time_str =("25th march 10am")
    matches = list(datefinder.find_dates(start_time_str))
    start_time_m = matches[0]
    start_time = start_time_m.strftime("%I:%M %p")
    #start_time_ = convert_time(start_time)
    #end_time_ = (datetime.datetime.combine(datetime.date.today(), start_time_) + datetime.timedelta(hours=2)).time()
    start = start_time
    end = "11PM"

    #end = end_time_.strftime("%I:%M %p")    

    event_result = service.events().insert(calendarId='primary',
       body={
           "summary": 'Automating calendar',
           "description": 'This is a tutorial example of automating google calendar with python',
           "start": {"dateTime": start, "timeZone": 'Africa/Nairobi'},
           "end": {"dateTime": end, "timeZone": 'Africa/Nairobi'},
       }
    ).execute()

    print("created event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])

if __name__ == '__main__':
   main()