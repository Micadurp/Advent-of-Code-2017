"""
Advent of Code Day 3 tests
"""
import pytest
from advent import day3

class TestDay3(object):
    """
    Tests day 3 solution using examples from problem description
    """
    
    def test_steps_1(self):
        """
        First bullet in problem description
        """
        result = day3.get_steps(1)
        assert result == 0

    def test_steps_2(self):
        """
        Second bullet in problem description
        """
        result = day3.get_steps(12)
        assert result == 3

    def test_steps_3(self):
        """
        Second bullet in problem description
        """
        result = day3.get_steps(23)
        assert result == 2

    def test_steps_4(self):
        """
        Second bullet in problem description
        """
        result = day3.get_steps(1024)
        assert result == 31
