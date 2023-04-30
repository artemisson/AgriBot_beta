import datetime

matches = {
    'team1': {
        'name': 'Team A',
        'time': '10:00am'
    },
    'team2': {
        'name': 'Team B',
        'time': '2:30pm'
    }
}

# Function to convert time in am/pm format to 24-hour format
def convert_time(time_str):
    time_obj = datetime.datetime.strptime(time_str, '%I:%M%p')
    return time_obj.time()

# Get the start time and end time for each match
for team in matches.values():
    start_time = convert_time(team['time'])
    end_time = (datetime.datetime.combine(datetime.date.today(), start_time) + datetime.timedelta(hours=2)).time()
    print(f"Match between {team['name']} starts at {start_time.strftime('%H:%M')} and ends at {end_time.strftime('%H:%M')}")
