"""
Advent of Code Day 1 part 2 tests
"""

from advent import day1

class TestDay1Part2(object):
    """
    Tests day 1 solution using examples from part 2's problem description
    """

    def test_halfway_1(self):
        """
        First bullet in part 2's problem description
        """
        test_data = [1, 2, 1, 2]
        halfway_of_array = int(len(test_data)/2)
        result = day1.sum_n_forward_same(test_data, halfway_of_array)
        assert result == 6

    def test_halfway_2(self):
        """
        Second bullet in part 2's problem description
        """
        test_data = [1, 2, 2, 1]
        halfway_of_array = int(len(test_data)/2)
        result = day1.sum_n_forward_same(test_data, halfway_of_array)
        assert result == 0

    def test_halfway_3(self):
        """
        Third bullet in part 2's problem description
        """
        test_data = [1, 2, 3, 4, 2, 5]
        halfway_of_array = int(len(test_data)/2)
        result = day1.sum_n_forward_same(test_data, halfway_of_array)
        assert result == 4

    def test_halfway_4(self):
        """
        Fourth bullet in part 2's problem description
        """
        test_data = [1, 2, 3, 1, 2, 3]
        halfway_of_array = int(len(test_data)/2)
        result = day1.sum_n_forward_same(test_data, halfway_of_array)
        assert result == 12

    def test_halfway_5(self):
        """
        Fifth bullet in part 2's problem description
        """
        test_data = [1, 2, 1, 3, 1, 4, 1, 5]
        halfway_of_array = int(len(test_data)/2)
        result = day1.sum_n_forward_same(test_data, halfway_of_array)
        assert result == 4
