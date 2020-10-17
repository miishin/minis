from re import search
from sys import argv
from twilio.rest import Client
import event, os
from json import load


def is_email(txt):
    return not search("[a-z]+[.]{1}[a-z]+@{1}northeastern.edu$", txt) is None


def is_username(txt):
    return not search("[a-z]+[.]{1}[a-z]+", txt) is None


# Opens the file of phone numbers
def get_numbers():
    f = open('numbers.json')
    return load(f)


def get_username(email):
    return email.split('@')[0]


# Creates the Twilio client using the env variables so
# sid/token are not on Git
def create_client():
    sid = os.environ["TWILIO_ACCOUNT_SID"]
    token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(sid, token)
    return client


# The phone number of the phone these texts will be sent from
def my_number():
    return os.environ['PHONE_NUMBER']


# Takes a file name and returns an Event object from it
def file_to_event(filename):
    f = open(filename)
    details = load(f)
    evt = event.Event(details['title'], details['date_time'], details['location'], details['description'], \
        details['fb_link'], details['zoom_link'])
    return evt