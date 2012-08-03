from django.test import TestCase

from stream_app.models import Stream

class StreamAppTestCase(TestCase):
    def setUp(self):
        super(StreamAppTestCase, self).setUp()
        print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
        for s in Stream.objects.all():
            print s
        print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
        self.stream1 = Stream.objects.get(pk='501acc4b70a2e42ec1e05092')
        print self.stream1

    def test_name_length(self):
        s = self.stream1
        self.assertTrue(len(s.name) > 1)
        self.assertTrue(len(s.name) < 80)
        
