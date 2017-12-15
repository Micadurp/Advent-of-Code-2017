#!/usr/bin/env python3
"""
Advent of Code Day 3 solution
"""

def get_steps(location):
    """
    Get amount of steps to get to location.
    """
    steps = 0
    if location != 1:
        steps_out, start_of_level = find_level(location)
        steps += steps_out

        unadjusted_location_in_edge = (location - start_of_level) % (2 * steps_out)
        adjusted_location_in_edge = unadjusted_location_in_edge - steps_out
        steps += abs(adjusted_location_in_edge)
    return steps

def find_level_recursion(location, iteration, previous):
    """
    Recursively find how far out from center location is
    """
    value = (iteration*8) + previous
    if location > value:
        iteration += 1
        return find_level_recursion(location, iteration, value)
    else:
        return (iteration, previous)

def find_level(location):
    """
    Recursively find how far out from center location is
    """
    iteration = 1
    previous = 1
    value = (iteration*8) + previous
    while location > value:
        previous = value
        iteration += 1
        value = (iteration*8) + previous
    return (iteration, previous)

def find_next_value(value):
    """
    Find the value that comes after the given value
    """
    #Init layer 0 and 1
    array = [1, 1, 2, 4, 5, 10, 11, 23, 25]
    #Safety for dumb values
    if value < 25:
        for index, item in enumerate(array):
            if item == value:
                return array[index+1]
    index = 9
    while value > array[index]:
        next_value = array[index]
        next_value += int(index/8) + 1
        #if index % 1:
            #(iteration*8) + previous
        value
        index += 1
