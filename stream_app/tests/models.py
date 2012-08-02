from django.test import TestCase
import mongoengine

class StreamAppTestCase(TestCase):
    def setUp(self):
        super(StreamAppTestCase, self).setUp())
        self.stream1 = Stream.objects.get(pk='501acc4b70a2e42ec1e05092')

    def test_name_lenght(self):
