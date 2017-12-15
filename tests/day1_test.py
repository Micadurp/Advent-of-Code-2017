"""
Advent of Code Day 1 tests
"""

from advent import day1

class TestDay1(object):
    """
    Tests day 1 solution using examples from problem description
    """

    def test_adjacent_1(self):
        """
        First bullet in problem description
        """
        test_data = [1, 1, 2, 2]
        result = day1.sum_n_forward_same(test_data)
        assert result == 3

    def test_adjacent_2(self):
        """
        Second bullet in problem description
        """
        test_data = [1, 1, 1, 1]
        result = day1.sum_n_forward_same(test_data)
        assert result == 4

    def test_adjacent_3(self):
        """
        Third bullet in problem description
        """
        test_data = [1, 2, 3, 4]
        result = day1.sum_n_forward_same(test_data)
        assert result == 0

    def test_adjacent_4(self):
        """
        Fourth bullet in problem description
        """
        test_data = [9, 1, 2, 1, 2, 1, 2, 9]
        result = day1.sum_n_forward_same(test_data)
        assert result == 9
