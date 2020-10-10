from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import json
import util

app = Flask(__name__)

links = {}

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


if __name__ == '__main__':
    links = build_links()
    app.run(host='0.0.0.0', port=80)
