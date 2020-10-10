## Event Texts
Important to have:
.env file for TWILIO authentication (not on Git for obvious reasons)

numbers.json - a file consisting of just a list of phone numbers, formatted as: "+XXXXXXXXXXX"

Create an event using eventconstructor.py by filling in info, this will create an event-name.json

Send event details to all phone numbers in numbers.json with sendevent.py (just give it the event-name.json)

## Zoom Link Distribution

This is in app.py

People will text their email address or just their username (which is just the email without the @...). 
Program will send back a zoom link according to a premade grouping. 

Currently running locally (not good). 

Of course, if those people aren't registered they should not receive a zoom link.