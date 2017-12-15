#!/usr/bin/env python3
"""
Advent of Code Day 2 solution
"""

def format_data(data_to_format):
    """
    Cleans and formats the data for the day.
    """
    formated_data = []
    for line in data_to_format:
        formated_data.append(list(map(int, line.split('\t'))))
    return formated_data

def get_checksum_from_2d_array(array):
    """
    Gets checksum from a 2d array
    """
    checksum = 0
    for row in array:
        checksum += max(row) - min(row)
    return checksum

def get_and_divide_evenly_divisable(array):
    """
    Finds 2 values that are evenly divisable and divides them
    """
    value = 0
    found = False
    for index, item in enumerate(array):
        for other_index, other_item in enumerate(array):
            if index != other_index:
                if item%other_item == 0:
                    value = item/other_item
                    found = True
                    break
                elif other_item%item == 0:
                    value = other_item/item
                    found = True
                    break
        if found is True:
            break
    return int(value)

def get_evenly_divisable_rowsum(array):
    """
    Checks for two values that are evenly divisable in each row, divides them,
    and returns the sum of the divided values
    """
    value_sum = 0
    for row in array:
        value_sum += get_and_divide_evenly_divisable(row)
    return value_sum
