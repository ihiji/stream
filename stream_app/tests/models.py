from django.test import TestCase
from stream_app.models import Stream, Word, Link
import time

class StreamAppTestCase(TestCase):
    def setUp(self):
        super(StreamAppTestCase, self).setUp()
        self.stream1 = Stream.objects.get(name='food')

        self.ts, was_created = Stream.objects.get_or_create(name='testStream')
        self.ts.start_time  = time.time()
        self.ts.end_time    = time.time() + 12
        self.ts.entries     = ['foo', 'bar', 'baz']
        self.ts.hits        = 1
        self.ts.entry_count = len(self.ts.entries)
        self.ts.save()

    def test_name_length(self):
        s = self.stream1
        self.assertTrue(len(s.name) > 1)
        self.assertTrue(len(s.name) < 80)

    def test_push_down_1(self):
        self.assertIsNotNone(Stream.objects.get(name='testStream'))
        # have to push down for links to show up
        self.assertTrue(Link.objects(lead_in='foo').count() is 0
                     or self.ts in Link.objects(lead_in='foo').first().streams)

        self.ts.push_down_info()
        k = Link.objects(lead_in='foo').first()
        self.assertIn(self.ts, k.streams)

        w = Word.objects(word='foo').first()
        self.assertTrue(self.ts in w.streams)

