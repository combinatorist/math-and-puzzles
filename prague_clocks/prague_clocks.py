import warnings
from itertools import cycle

citation = {
        'journal'      : 'The Mathematical Intelligencer',
        'volume'       : 38,
        'number'       : 1,
        'season'       : 'Spring',
        'year'         : 2016,
        'title'        : 'Prague Clocks',
        'first_author' : 'Chan Bae',
    }


def triangular_num_list(n):
    """
    finds the first n triangular numbers
    """
    num_list = []
    cumulative = 0
    for num in range(n):
        cumulative = cumulative + num
        num_list.append(cumulative)
    return num_list


def modulo_list(modulo, num_list=None, append_m=True):
    """
    reduces the first modulo-1 triangular numbers mod modulo
    """
    if num_list is None:
        num_list = triangular_num_list(modulo)
    num_list = sorted(set(num % modulo for num in num_list))
    if append_m:
        num_list.append(modulo)
    return num_list


def prague_clock(modulo=None, num_list=None):
    """
    sorts and calculates differences given a modulo
    """
    if modulo is not None:
        if num_list is not None:
            warnings.warn('num_list argument overwridden by modulo argument')
        num_list = modulo_list(modulo)
    if num_list is None:
        warnings.warn("arguments modulo and num_list can't both be None")
    num_list = sorted(num_list)
    diff_list = []
    for i in range(1, len(num_list)):
        diff_list.append(num_list[i] - num_list[i - 1])
    return diff_list

def demo(hour, prague_clock, modulo=None, show_all=True):
    """
    demonstrates a number based on a prague clock"
    """
    if modulo is None:
        if prague_clock is None:
            warnings.warn("demo arguments modulo and prague_clock can't both be None")
        modulo = sum(prague_clock)

    prague_clock = cycle(prague_clock)
    chime_schedule = []
    for num in range(1, hour + 1):        
        chime_pattern = []
        while sum(chime_pattern) < num:
            chime_pattern.append(prague_clock.next())
            if sum(chime_pattern) > num:
                raise RuntimeError("No chime pattern could be found for the given hour. Check that you provided a valid prague clock.")
        chime_schedule.append(chime_pattern)
    if show_all:
        return chime_schedule
    else:
        return chime_schedule[-1]
        
