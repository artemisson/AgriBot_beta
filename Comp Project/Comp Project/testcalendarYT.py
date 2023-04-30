from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

scopes = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file("credentials.json", scopes = scopes)
credentials = flow.run_local_server()

#ensuring credentials access instead of reauthentication
import pickle
pickle.dump(credentials,open("token.pkl", "wb"))
credentials = pickle.load(open("token.pkl", "rb"))
service = build("calendar", "v3", credentials =credentials)

#GET MY CALENDARS
result = service.calendarList().list().execute()
result['items'][0]

#CREATE CALENDAR EVENTS
import datefinder
def create_event(start_time_str, summary, duration=1, description=None, location=None):
    matches = datefinder.find_dates("5th May 9PM")
    list(matches)
    
    if len(matches):
        start_time = matches[0]
        end_time = start_time + timedelta(hours = duration)
    
    event = {
        'summary' : summmary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Africa/Kenya',
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': 'Africa/Kenya',
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