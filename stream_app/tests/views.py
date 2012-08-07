from django.test import TestCase

class StreamAppViewTestCase(TestCase):
    def setUp(self):
        pass

    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
