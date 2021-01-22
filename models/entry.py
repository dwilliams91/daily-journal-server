class Entry():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, date, topic, entry, mood_id, hashtag_id ):
        self.id = id
        self.date = date
        self.topic = topic
        self.entry = entry
        self.mood_id = mood_id
        self.hashtag_id = hashtag_id
        