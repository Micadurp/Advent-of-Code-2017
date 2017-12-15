"""
Advent of Code Day 2 tests
"""
import pytest
from advent import day2

# pylint: disable=redefined-outer-name

@pytest.fixture
def day2_data():
    """
    Creates day 2 test data
    """
    test_data = []
    test_data.append([5, 1, 9, 5])
    test_data.append([7, 5, 3])
    test_data.append([2, 4, 6, 8])
    return test_data

@pytest.fixture
def day2part2_data():
    """
    Creates day 2 test data
    """
    test_data = []
    test_data.append([5, 9, 2, 8])
    test_data.append([9, 4, 7, 3])
    test_data.append([3, 8, 6, 5])
    return test_data

class TestDay2(object):
    """
    Tests day 2 solution using examples from problem description
    """

    def test_checksum_1(self, day2_data):
        """
        First bullet in problem description
        """
        result = day2.get_checksum_from_2d_array(day2_data)
        assert result == 18

    def test_evenly_divisable_row_1(self, day2part2_data):
        """
        First bullet in problem description
        """
        result = day2.get_and_divide_evenly_divisable(day2part2_data[0])
        assert result == 4

    def test_evenly_divisable_row_2(self, day2part2_data):
        """
        Second bullet in problem description
        """
        result = day2.get_and_divide_evenly_divisable(day2part2_data[1])
        assert result == 3

    def test_evenly_divisable_row_3(self, day2part2_data):
        """
        Third bullet in problem description
        """
        result = day2.get_and_divide_evenly_divisable(day2part2_data[2])
        assert result == 2

    def test_evenly_divisable_sum_1(self, day2part2_data):
        """
        Sum of all rows
        """
        result = day2.get_evenly_divisable_rowsum(day2part2_data)
        assert result == 9
