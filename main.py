#http://amgcomputing.blogspot.com/2012/11/retrieving-google-calendar-events-with.html
#http://stackoverflow.com/questions/22746733/how-to-authorize-installed-app-for-biqquery-with-google-oauth

calendarId = 'constantinz@gmail.com'

import google_calendar
import pprint

def getEvents(pageToken=None):
    events = google_calendar.service.events().list(
        calendarId=calendarId,
        singleEvents=True,
        maxResults=1,
        orderBy='startTime',
        timeMin='2014-07-01T00:00:00-08:00',
        timeMax='2014-07-15T00:00:00-08:00',
        pageToken=pageToken,
        ).execute()
    return events

def main():
    events = getEvents()
    while True:
        for event in events['items']:
            #pprint.pprint(event)
            #https://developers.google.com/google-apps/calendar/v3/reference/events/instances?hl=zh-TW
            print '  '
            print event['start']
            print event['end']
            print event['summary']
            print '  '
        page_token = events.get('nextPageToken')
        if page_token:
            events = getEvents(page_token)
        else:
            break

if __name__ == '__main__':
    main()