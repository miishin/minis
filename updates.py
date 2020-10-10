import util

def send_message(numbers, message):
    client = util.create_client()
    my_number = util.my_number()
    for phone in numbers:
        response = client.messages.create(
            body=message,
            from_=my_number,
            to=phone
        )


def send_event(jsonfile):
    event = util.file_to_event(jsonfile)
    send_message(util.get_numbers(), event.format_text())




