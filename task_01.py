#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Does some math and returns a string in response.

    Args:
        wink (str): Arg to be arithmetically factored by numwink.
        nudges (str): Arg to be airthmeticaly factored by numwink. Default: 2
        retstr (str): Arg formatted to input winks, nudges.
        
    Returns:
        string from retstr.

    Examples:

        >>> know_what_i_mean('hello')
        'Know what I mean? hellohello, nudge nudge'
    
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr

