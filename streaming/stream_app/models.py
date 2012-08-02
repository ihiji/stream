from mongoengine import *

class Stream(Document):
    entries = ListField(StringField(regex='[a-zA-Z]{1,40}'))
    '''
    start_time = time thinger
    end_time
    entry_count = 
    '''
    

class User(Document):
    email = EmailField()
