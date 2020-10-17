from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import json

app = Flask(__name__)

links = {}
numbers = []

@app.route("/", methods=['GET', 'POST'])
def receive():
    phone_number = request.values.get('From', None)
    message_body = request.values.get('Body', None)

    resp = MessagingResponse()

    if is_subscribe(message_body):
        if phone_number not in numbers:
            numbers.append(phone_number)
            update_numbers_file()
            resp.message("You are now subscribed to receive updates for ASU Minis :)")
        else:
            resp.message("You are already subscribed!")
    elif is_unsubscribe(message_body):
        if phone_number in numbers:
            numbers.remove(phone_number)
            update_numbers_file()
        else:
            resp.message("You were not subscribed to begin with!")
    elif phone_number in numbers:
        resp.message("I'm not a real person so you won't get anything from texting me :)\nText 'STOP' to unsubscribe.")
    else:
        resp.message("Subscribe for updates by sending 'MINIS'\nUnsubscribe with 'STOP'")

    return str(resp)

def is_subscribe(message):
    msg = message.lower()
    return msg == "minis"

def is_unsubscribe(message):
    msg = message.lower()
    return msg == "stop"

def update_numbers_file():
    json_file = open('numbers.json', 'w')
    json.dump(numbers, json_file)

def open_numbers_file():
    json_file = open('numbers.json', 'r')
    return json.load(json_file)


"""
@app.route("/", methods=['GET', 'POST'])
def sms_reply():
    message_body = request.values.get('Body', None)

    resp = MessagingResponse()

    # We just want the username to get the proper zoom link
    if util.is_email(message_body):
        username = util.get_username(message_body)
        resp.message(get_zoom_link(username))
    elif util.is_username(message_body):
        resp.message(get_zoom_link(message_body))
    else:
        parsed_message = "Please provide your @northeastern.edu email or the username (email w/o the @northeastern.edu)"
        resp.message(parsed_message)
    return str(resp)


# Gets the zoom link matched to the given username
def get_zoom_link(username):
    if username in links:
        return links[username]
    else:
        return "Your email was not found"

# Opens the file containing all the pairings and loads it in
def build_links():
    json_file = open('links.json')
    return json.load(json_file)
"""

if __name__ == '__main__':
    numbers = open_numbers_file()
    app.run(host='0.0.0.0', port=80)
