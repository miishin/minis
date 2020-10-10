# A representation of a usual event
class Event():

    def __init__(self, title, date_time, location, description, fb_link, zoom_link=None):
        self.title = title
        self.date_time = "When: " + date_time
        self.location = "Where: " + location
        self.description = description
        self.fb = "Facebook Event Link:\n" + fb_link
        self.zoom = "Zoom Link:\n" + zoom_link

    # Returns a text representation of this event (to be sent in a text)
    def format_text(self):
        return '\n'.join([self.title, self.date_time, self.location, self.description, self.fb, self.zoom])