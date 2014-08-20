import gflags
import httplib2

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run

FLAGS = gflags.FLAGS

# Set up a Flow object to be used if we need to authenticate. This
# sample uses OAuth 2.0, and we set up the OAuth2WebServerFlow with
# the information it needs to authenticate. Note that it is called
# the Web Server Flow, but it can also handle the flow for native applications
# The client_id and client_secret are copied from the API Access tab on the Google APIs Console
FLOW = OAuth2WebServerFlow(
        client_id='288731703258-poangubgqp6loqvdpkgs1jisuog2d8tj.apps.googleusercontent.com',
        client_secret='V5--hpsioUavSdkCLmALmyjR',
        scope='https://www.googleapis.com/auth/calendar',
        user_agent='Python/2.7')
# To disable the local server feature, uncomment the following line:
FLAGS.auth_local_webserver = False

# If the Credentials don't exist or are invalid, run through the native client
# flow. The Storage object will ensure that if successful the good
# Credentials will get written back to a file.
storage = Storage('client_secret.dat')
credentials = storage.get()
if credentials is None or credentials.invalid == True:
    credentials = run(FLOW, storage)

# Create an httplib2.Http object to handle our HTTP requests and authorize it with our good Credentials.
http = httplib2.Http()
print http
http = credentials.authorize(http)

# Build a service object for interacting with the API. Visit
# the Google APIs Console to get a developerKey for your own application.
service = build(serviceName='calendar', version='v3', http=http, developerKey='AIzaSyAz3m7ibbPbHcXRnDeIu43zmYey04z81PU')
kudos_calendar = None
try:
    kudos_calendar = service.calendarList().get(calendarId='constantinz@gmail.com').execute()
except:
    print 'Calendar KudosCalendar does not exist!'
    print 'Creating one right now...'
    kudos_calendar_entry = {
        'id': 'KudosCalendar'
    }

    kudos_calendar = service.calendarList().insert(body=kudos_calendar_entry).execute()