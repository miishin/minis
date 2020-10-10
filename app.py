from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import json
import util

app = Flask(__name__)

links = {}

@app.route("/", methods=['GET', 'POST'])
def sms_reply():
    number = request.values.get('From', None)
    message_body = request.values.get('Body', None)

    resp = MessagingResponse()

    if util.is_email(message_body):
        username = util.get_username(message_body)
        resp.message(get_zoom_link(username))
    elif util.is_username(message_body):
        resp.message(get_zoom_link(message_body))
    else:
        parsed_message = "Please provide your @northeastern.edu email or the username (email w/o the @northeastern.edu)"
        resp.message(parsed_message)
    return str(resp)


def get_zoom_link(username):
    if username in links:
        return links[username]
    else:
        return "Your email was not found"


def build_links():
    json_file = open('links.json')
    return json.load(json_file)




if __name__ == '__main__':
    links = build_links()
    app.run(host='0.0.0.0', port=80)
