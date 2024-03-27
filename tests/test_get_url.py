import unittest
from src.utils.url import get_ziprecruiter_url

class TestGetZipRecruiterUrl(unittest.TestCase):

    def test_valid_input(self):
        """Test the function with valid inputs."""
        url = get_ziprecruiter_url('engineer', 'New York', 'NY', '', 0, '5', '30', '100000', 0)
        expected_url = "https://www.ziprecruiter.com/jobs-search?form=jobs-landing&search=engineer&location=New+York%2C+NY&radius=5&days=30&refine_by_salary=100000&refine_by_employment=employment_type%3Aall"
        self.assertEqual(url, expected_url)

    def test_invalid_state(self):
        """Test the function with an invalid state."""
        with self.assertRaises(ValueError):
            get_ziprecruiter_url('engineer', 'New York', 'XX', '', 0, '5', '30', '100000', 0)

    def test_invalid_refine_by_location_index(self):
        """Test the function with an invalid refine_by_location_index."""
        with self.assertRaises(ValueError):
            get_ziprecruiter_url('engineer', 'New York', 'NY', '', 3, '5', '30', '100000', 0)

    def test_invalid_refine_by_employment_index(self):
        """Test the function with an invalid refine_by_employment_index."""
        with self.assertRaises(ValueError):
            get_ziprecruiter_url('engineer', 'New York', 'NY', '', 0, '5', '30', '100000', 3)

if __name__ == '__main__':
    unittest.main()
