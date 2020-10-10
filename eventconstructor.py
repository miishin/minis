from json import dump

def main():
    data = {}
    data['title'] = input("Name of event:\n")
    data['date_time'] = input("Date/Time of event:\nFollow format MM/DD/YY HH:MM PM/AM\n")
    data['location'] = input("Location of event:\n")
    data['description'] = input("Description of event:\n")
    data['fb_link'] = input("Facebook event link:\n")
    data['zoom_link']= input("Zoom meeting link:\n")
    nickname = input("Give a short nickname for this event:\n")
    filename = nickname + ".json"
    dump(data, open(filename, 'w'))

if __name__ == '__main__':
    main()