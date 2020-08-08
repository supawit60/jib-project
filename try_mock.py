import unittest
from unittest.mock import patch
from try_import_mock import get_number_1
from try_import_mock import get_random_number_plus_one


class TestRandom(unittest.TestCase):
    @patch('try_import_mock.random.randint')
    def test_it_should_call_randint_with_1_and_10(self, mock):
        get_random_number_plus_one()
        mock.assert_called_once_with(1, 5)
        # assert here

    @patch('try_import_mock.random.randint')
    def test_it_should_get_4_when_randint_get_3(self, mock):
        mock.return_value = 3
        result = get_random_number_plus_one()
        self.assertEqual(result, 4)
        # assert here

    # @patch('try_import_mock.get_number_1')
    # def test_get_number_other_file(self, mock):
    #     mock.return_value = 2
    #     result = get_number_1()
    #     self.assertEqual(result, 2)

    def test_it_should_get_3(self):
        while True:
            result = get_random_number_plus_one()
            if result == 3:
                break

        self.assertEqual(result, 3)


unittest.main()
