#!/usr/bin/env python3
"""Core for Advent of Code 2017"""

import argparse
import os
import sys

from advent import day1
from advent import day2
from advent import day3

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def day1_case():
    """
    Run day 1 case
    """
    print("Day 1 Start")
    with open(os.path.join(__location__, "Data/day1data.txt"), "r") as daydata:
        formated_daydata = day1.format_data(daydata)
    print("1 step: ", day1.sum_n_forward_same(formated_daydata))
    halfway = int(len(formated_daydata)/2)
    print("Halfway: ", day1.sum_n_forward_same(formated_daydata, halfway))
    print("Day 1 Done")

def day2_case():
    """
    Run day 2 case
    """
    print("Day 2 Start")
    with open(os.path.join(__location__, "Data/day2data.txt"), "r") as daydata:
        formated_daydata = day2.format_data(daydata)
    print("Checksum:", day2.get_checksum_from_2d_array(formated_daydata))
    print("Evenly divisable rowsum:", day2.get_evenly_divisable_rowsum(formated_daydata))
    print("Day 2 Done")

def day3_case():
    """
    Run day 3 case
    """
    print("Day 3 Start")
    #print("Steps:", day3.get_steps(325489))
    print("Steps:", day3.get_steps(36807888888888))

def default_case(day):
    """
    Run default case
    """
    print("Day", day, "hasn't been implemented")

# map the inputs to the function blocks
ADVENT_DAYS = {
    1 : day1_case,
    2 : day2_case,
    3 : day3_case
}

def start():
    """
    Start!
    """
    parser = argparse.ArgumentParser(description="Run your choice of advent of code days!")
    parser.add_argument("days", metavar="N", type=int, nargs="+",
                        help="the day you want")
    args = parser.parse_args()

    for day in args.days:
        advent_case = ADVENT_DAYS.get(day, default_case)
        if advent_case != default_case:
            advent_case()
        else:
            advent_case(day)
