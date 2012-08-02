from mongoengine import *
from mongoengine.django.auth import User

class Stream(Document):
    name    = StringField(min_length=1, max_length=80, help_text="A Name to find your stream")
    entries = ListField(StringField(regex='[a-zA-Z]{1,40}'))
    start_time = DateTimeField()
    end_time   = DateTimeField()
    entry_count = IntField(min_value=0)
    user = ReferenceField('User', reverse_delete_rule=CASCADE)

    def __unicode__(self):
        return self.name
