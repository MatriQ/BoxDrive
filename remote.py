# coding: utf-8

from __future__ import print_function, unicode_literals
import os
from boxsdk import Client
from boxsdk.exception import BoxAPIException
from boxsdk.object.collaboration import CollaborationRole
from auth import authenticate

def get_events(client):
    print(client.events().get_events(limit=100, stream_position='now'))


def get_latest_stream_position(client):
    print(client.events().get_latest_stream_position())

def run_examples(oauth):

    client = Client(oauth)
    get_events(client)
    get_latest_stream_position(client)

    for event in client.events().generate_events_with_long_polling():
        print('------------------------------------------------')
        print('New notification arrived!')
        print('Event type ' + event.get('event_type',''))
        print('File hash ' + event.get('source').get('sha1',''))
        print('File name ' + event.get('source').get('name',''))
        print('File type ' + event.get('source').get('type',''))

        absolutePath = '';

        for directory in event.get('source').get('path_collection').get('entries'):
            absolutePath = absolutePath +'/'+ directory.get('name')

        print('Path ' + '"' + absolutePath + '"')
        print('All info below:')
        print(event)
        print('------------------------------------------------')

def main():

    # Please notice that you need to put in your client id and client secret in demo/auth.py in order to make this work.
    oauth = authenticate()
    run_examples(oauth)
    os._exit(0)

if __name__ == '__main__':
    main()
