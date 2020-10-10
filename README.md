Important to have:
.env file for TWILIO authentication (not on Git for obvious reasons)

numbers.json - a file consisting of just a list of phone numbers, formatted as: "+XXXXXXXXXXX"

Create an event using eventconstructor.py by filling in info, this will create an event-name.json

Send event details to all phone numbers in numbers.json with sendevent.py (just give it the event-name.json)