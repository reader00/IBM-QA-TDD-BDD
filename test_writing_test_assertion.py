from unittest import TestCase
from triangle import area_of_a_triangle


class TestAreaOfTriangle(TestCase):

    def test_good_values(self):
        """ Test area when values are good """

        self.assertAlmostEqual(area_of_a_triangle(3.4556, 8.3567), 14.43870626)
        self.assertEqual(area_of_a_triangle(2, 5), 5.0)
        self.assertEqual(area_of_a_triangle(0, 5), 0.0)

    def test_bad_values(self):
        """ Test area when values are bad """

        self.assertRaises(ValueError, area_of_a_triangle, -2, 5)
        self.assertRaises(ValueError, area_of_a_triangle, 3, -1)

    def test_bad_types(self):
        """ Test area when types are bad """

        self.assertRaises(TypeError, area_of_a_triangle, "", 1)
        self.assertRaises(TypeError, area_of_a_triangle, 3, [])
        self.assertRaises(TypeError, area_of_a_triangle, 3, True)
        self.assertRaises(TypeError, area_of_a_triangle, {}, 10)
