from datetime import datetime, timedelta
import datefinder
import datetime

def convert_time(start_time):
    time_obj = datetime.datetime.strptime(start_time, "%I:%M %p")
    return time_obj.time()

def create_event():
    start_time_str =("25th march 10am")
    matches = list(datefinder.find_dates(start_time_str))
    start_time_m = matches[0]
    # Format the start time as AM/PM and print it
    start_time = start_time_m.strftime("%I:%M %p")
    end_time = start_time_m + timedelta(hours=4)
    #start_time_ = convert_time(start_time)
    #end_time_ = (datetime.datetime.combine(datetime.date.today(), start_time_) + datetime.timedelta(hours=2)).time()
    #_start_time = start_time_.strftime("%Y-%m-%dT%H:%M:%S")
    #_end_time = end_time_.strftime("%Y-%m-%dT%H:%M:%S")
    #print("Start Time:", start_time_.strftime("%Y-%m-%dT%H:%M:%S"))
    #print("End Time:", end_time_.strftime("%Y-%m-%dT%H:%M:%S"))
    print(matches[0])
    print(start_time_m)
    print(end_time)
    #print("Start Time:", start_time_.strftime('%H:%M'))
    #print("End Time:", end_time_.strftime('%H:%M'))
    #print(matches)
    #print(f"Match between starts at {start_time_.strftime('%H:%M')} and ends at {end_time_.strftime('%H:%M')}")
create_event()