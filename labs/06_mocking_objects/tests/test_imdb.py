"""
Test Cases for Mocking Lab
"""
import json
from unittest import TestCase
from unittest.mock import patch, Mock
from requests import Response
from models import IMDb

IMDB_DATA = {}


class TestIMDbDatabase(TestCase):
    """Tests Cases for IMDb Database"""

    @classmethod
    def setUpClass(cls):
        """ Load imdb responses needed by tests """
        global IMDB_DATA
        with open('tests/fixtures/imdb_responses.json') as json_data:
            IMDB_DATA = json.load(json_data)

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    # Mock: Bypass search_titles, GOOD_SEARCH

    @patch("test_imdb.IMDb.search_titles")
    def test_search_titles(self, imdb_mock):
        """ Test searching by title """
        imdb_mock.return_value = IMDB_DATA["GOOD_SEARCH"]
        imdb = IMDb("k_12345678")

        results = imdb.search_titles("Bambi")
        self.assertIsNotNone(results)
        self.assertIsNone(results['errorMessage'])
        self.assertIsNotNone(results['results'])
        self.assertEqual(results['results'][0]['id'], "tt1375666")

    # Mock: 404

    @patch("models.imdb.requests.get")
    def test_search_with_no_results(self, imdb_mock):
        """ Test searching with no results """
        imdb_mock.return_value = Mock(status_code=404)
        imdb = IMDb('k_12345678')
        results = imdb.search_titles("Uga Buga")
        self.assertEqual(results, {})

    # Mock: 200, INVALID_API

    @patch("models.imdb.requests.get")
    def test_search_by_title_failed(self, imdb_mock):
        """ Test searching by title failed """
        imdb_mock.return_value = Mock(
            spec=Response,
            status_code=200,
            json=Mock(return_value=IMDB_DATA['INVALID_API'])
        )
        imdb = IMDb('bad-key')
        results = imdb.search_titles("Bambi")
        self.assertIsNotNone(results)
        self.assertEqual(results['errorMessage'], "Invalid API Key")

    # Mock: 200, GOOD_RATING

    @patch("models.imdb.requests.get")
    def test_movie_rating(self, imdb_mock):
        """ Test movie rating """
        imdb_mock.return_value = Mock(
            spec=Response,
            status_code=200,
            json=Mock(return_value=IMDB_DATA['GOOD_RATING'])
        )
        imdb = IMDb('key_12345678')
        results = imdb.movie_ratings("tt1375666")
        self.assertIsNotNone(results)
        self.assertEqual(results['title'], "Bambi")
        self.assertEqual(results['theMovieDb'], 4)
        self.assertEqual(results['filmAffinity'], 3)
        self.assertEqual(results['rottenTomatoes'], 5)

    # Mock: 404

    @patch("models.imdb.requests.get")
    def test_movie_rating_not_found(self, imdb_mock):
        """ Test movie rating not found """
        imdb_mock.return_value = Mock(
            spec=Response,
            status_code=404
        )
        imdb = IMDb('key_12345678')
        results = imdb.movie_ratings("asdasdasd")
        self.assertDictEqual(results, {})

    # Mock: 200, GOOD_REVIEW

    @patch("models.imdb.requests.get")
    def test_movie_review(self, imdb_mock):
        """ Test movie reviews """
        imdb_mock.return_value = Mock(
            spec=Response,
            status_code=200,
            json=Mock(return_value=IMDB_DATA['GOOD_REVIEW'])
        )
        imdb = IMDb('key_12345678')
        results = imdb.movie_reviews("tt1375666")
        self.assertIsNotNone(results)
        self.assertEqual(results['title'], "Bambi")
        self.assertEqual(results['items'][0]['username'], 'mickey')
        self.assertEqual(results['items'][0]['content'],
                         'This movie will make you cry')

    # Mock: 404

    @patch("models.imdb.requests.get")
    def test_movie_review_not_found(self, imdb_mock):
        """ Test movie reviews not found """
        imdb_mock.return_value = Mock(
            spec=Response,
            status_code=404
        )
        imdb = IMDb('key_12345678')
        results = imdb.movie_reviews("asdasdasd")
        self.assertDictEqual(results, {})
