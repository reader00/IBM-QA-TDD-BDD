from unittest import TestCase


class TestAccoundModule(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # Connect to database
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        # Disconnect from databse
        return super().tearDownClass()

    def setUp(self) -> None:
        # Drop table and create
        return super().setUp()

    def tearDown(self) -> None:
        # Remove session and drop table
        return super().tearDown()
