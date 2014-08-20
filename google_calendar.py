client_id='1009266176955-hf0abknk6bksur38k4ci2841eas2o9sh.apps.googleusercontent.com'
client_secret='MB3nMJTiH9VvqpfNgaM8VQhx'
user_agent='Python/2.7' 
developerKey='AIzaSyB5D66UxtE_funXZw7WKxvYKcfBxjIHOc0' 

import os.path
here = os.path.dirname(os.path.realpath(__file__))
storage_file = os.path.join(here, 'calendar.dat')

import gflags
import httplib2

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run

import sys
import argparse
from oauth2client import tools

FLAGS = gflags.FLAGS

# Set up a Flow object to be used if we need to authenticate. This
# sample uses OAuth 2.0, and we set up the OAuth2WebServerFlow with
# the information it needs to authenticate. Note that it is called
# the Web Server Flow, but it can also handle the flow for native
# applications
# The client_id and client_secret are copied from the API Access tab on
# the Google APIs Console
FLOW = OAuth2WebServerFlow(
    client_id=client_id,
    client_secret=client_secret,
    scope='https://www.googleapis.com/auth/calendar',
    user_agent=user_agent)

# To disable the local server feature, uncomment the following line:
FLAGS.auth_local_webserver = False

# If the Credentials don't exist or are invalid, run through the native client
# flow. The Storage object will ensure that if successful the good
# Credentials will get written back to a file.
storage = Storage(storage_file)
credentials = storage.get()
if credentials is None or credentials.invalid == True:
  #credentials = run(FLOW, storage)
  argparser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[tools.argparser])
  flags = argparser.parse_args(sys.argv[1:])
  credentials = tools.run_flow(FLOW, storage, flags)

# Create an httplib2.Http object to handle our HTTP requests and authorize it
# with our good Credentials.
http = httplib2.Http()
http = credentials.authorize(http)

# Build a service object for interacting with the API. Visit
# the Google APIs Console
# to get a developerKey for your own application.
service = build(serviceName='calendar', version='v3', http=http, developerKey=developerKey)
     