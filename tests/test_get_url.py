import unittest
from src.utils.url import get_ziprecruiter_url, get_monster_url, get_careerbuilder_url

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

class TestGetMonsterUrl(unittest.TestCase):

    def test_valid_input(self):
        """Test the function with valid inputs."""
        url = get_monster_url('engineer', 'New York', 'NY', 1, 0, 0)
        expected_url = "https://www.monster.com/jobs/search?q=engineer&where=New+York%2C+NY&page=1&et=FULL_TIME"
        self.assertEqual(url, expected_url)

    def test_invalid_state(self):
        """Test the function with an invalid state abbreviation."""
        with self.assertRaises(ValueError):
            get_monster_url('engineer', 'New York', 'XX', 1, 0, 0)

    def test_invalid_et_tuple_index(self):
        """Test the function with an invalid employment type index."""
        with self.assertRaises(ValueError):
            get_monster_url('engineer', 'New York', 'NY', 1, 5, 0)

    def test_invalid_recency_tuple_index(self):
        """Test the function with an invalid recency index."""
        with self.assertRaises(ValueError):
            get_monster_url('engineer', 'New York', 'NY', 1, 0, 6)

class TestGetCareerBuilderUrl(unittest.TestCase):

    def test_valid_input(self):
        """Test the function with valid inputs."""
        url = get_careerbuilder_url('1', 2, 'false', 'engineer', 'New York', 'NY', '60', 0, 'false', 0)
        expected_url = "https://www.careerbuilder.com/jobs?posted=1&radius=30&cb_apply=false&keywords=engineer&location=New+York%2C+NY&pay=60&emp=jtft%2Cjtfp&cb_veterans=false&cb_workhome=all"
        self.assertEqual(url, expected_url)

    def test_invalid_state(self):
        """Test the function with an invalid state abbreviation."""
        with self.assertRaises(ValueError):
            get_careerbuilder_url('1', 2, 'false', 'engineer', 'New York', 'XX', '60', 0, 'false', 0)

    def test_invalid_radius_tuple_index(self):
        """Test the function with an invalid radius tuple index."""
        with self.assertRaises(ValueError):
            get_careerbuilder_url('1', 4, 'false', 'engineer', 'New York', 'NY', '60', 0, 'false', 0)

    def test_invalid_emp_tuple_index(self):
        """Test the function with an invalid employment tuple index."""
        with self.assertRaises(ValueError):
            get_careerbuilder_url('1', 2, 'false', 'engineer', 'New York', 'NY', '60', 6, 'false', 0)

    def test_invalid_cb_workhome_tuple_index(self):
        """Test the function with an invalid work from home tuple index."""
        with self.assertRaises(ValueError):
            get_careerbuilder_url('1', 2, 'false', 'engineer', 'New York', 'NY', '60', 0, 'false', 4)

if __name__ == '__main__':
    unittest.main()
