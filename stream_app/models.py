from mongoengine import *
from mongoengine.django.auth import User

# TODO: think about deletes and references here

class Stream(Document):
    name    = StringField(min_length=1, max_length=80, help_text="A Name to find your stream")
    entries = ListField(StringField(regex='[a-zA-Z]{1,40}'))
    start_time = IntField() #timestamp
    end_time   = IntField() #timestamp
    entry_count = IntField(min_value=0)
    user = ReferenceField('User', reverse_delete_rule=CASCADE)

    def __unicode__(self):
        return self.name

    def push_down_info(stream):
        '''
        take apart the stream and push down the associated info and connections
        call this /after/ a stream has been full made
        '''
        entriesCount = len(stream.entries)
        for idx in range(entriesCount):
            entry = stream.entries[idx]
            word, was_created = Word.objects.get_or_create(word=entry)
            if self not in word.streams:
                word.streams.append(self)
            if idx > 0:
                previous = stream.entries[idx - 1]
                if previous not in word.lead_ins:
                    word.lead_ins.append(previous)
                k, k_was_created = Link.objects.get_or_create(lead_in=previous, follow_out=entry)
                if not k_was_created:
                    k.count += 1
                if self not in k.streams:
                    k.streams.append(self)
                k.save()
            if idx < entry_count - 1:
                next = stream.entries[idx + 1]
                if next not in word.follow_outs:
                    word.follow_outs.append(next)
                k, k_was_created = Link.objects.get_or_create(lead_in=entry, follow_out=next)
                if not k_was_created:
                    k.count += 1
                if self not in k.streams:
                    k.streams.append(self)
                k.save()
            word.save()


class Link(Document):
    follow_out = ReferenceField('Word')
    lead_in    = ReferenceField('Word')
    count      = IntField(min_value=1, default=1)
    streams    = ListField(ReferenceField('Stream', reverse_delete_rule=PULL))

    def __unicode__(self):
        return self.lead_in.word + '_' + self.follow_out.word


class Word(Document):
    word         = StringField(min_length=1, max_length=80, help_text="A Name to find your stream")
    links        = ReferenceField('Link')
    hits         = IntField(min_value=0, default=1)
    streams      = ListField(ReferenceField('Stream', reverse_delete_rule=PULL))
    stream_count = IntField(min_value=0)
    lead_ins     = ListField(StringField(regex='[a-zA-Z]{1,40}'))
    follow_outs  = ListField(StringField(regex='[a-zA-Z]{1,40}'))

    def __unicode__(self):
        return self.name
