"""
Test Cases for Counter Web Service

Create a service that can keep a track  of multiple counters
 - API must be RESTful
 - The endpoint should be called /counters
 - When creating a counter, you specify the name in the path
 - If the name being created already exists return a 409 Conflict

"""
from unittest import TestCase
from counter import app
import status


class CounterTest(TestCase):
    """ Counter tests """

    def setUp(self) -> None:
        self.client = app.test_client()

    def test_create_a_counter(self):
        """ Should create a counter """
        result = self.client.post("/counters/foo")

        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

    def test_duplicate_counter(self):
        """ Should return an error for duplicate """
        result = self.client.post("/counters/bar")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

        result = self.client.post("/counters/bar")
        self.assertEqual(result.status_code, status.HTTP_409_CONFLICT)
