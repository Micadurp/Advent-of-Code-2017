#!/usr/bin/env python3
"""
Advent of Code Day 1 solution
Will check how many digits are the same as the digit n steps forward in a circular array
"""

def format_data(data_to_format):
    """
    Cleans and formats the data for the day.
    """
    formated_data = list(map(int, data_to_format.read()))
    return formated_data

def sum_n_forward_same(array_of_numbers, steps=1):
    """
    Sums up amount of digits are the same as n steps forward in a circular array
    """
    digit_sum = 0
    for index, curr_nr in enumerate(array_of_numbers):
        if curr_nr == array_of_numbers[(index + steps) % len(array_of_numbers)]:
            digit_sum += curr_nr
    return digit_sum

def check_if_adjacent_same(array_of_numbers):
    """
    Deprected - used for part 1, but is replaced by new function
    Sums up amount of digits are the same as next digit in a circular array
    """
    digit_sum = 0
    prev_nr = 0
    for curr_nr in array_of_numbers:
        if prev_nr == curr_nr:
            digit_sum += curr_nr
        prev_nr = curr_nr
    if array_of_numbers[-1] == array_of_numbers[0]:
        digit_sum += array_of_numbers[0]
    return digit_sum
