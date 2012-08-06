from django.test import TestCase

from stream_app.models import Stream

class StreamAppTestCase(TestCase):
    def setUp(self):
        super(StreamAppTestCase, self).setUp()
        self.stream1 = Stream.objects.get(name='food')

    def test_name_length(self):
        s = self.stream1
        self.assertTrue(len(s.name) > 1)
        self.assertTrue(len(s.name) < 80)
        
