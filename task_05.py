#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module contatins function defaults."""


def defaults(my_required, my_optional=True):
    """False Testing function.

    Args:
        my_required (mixed): Compared for Truthiness.
        my_optional (bool, optional): Compared for Truthiness. Default = True

    Returns:
        bool: True if my _required is my_optional, else False.

    Examples:
        >>> defaults(True)
        True

        >>> defaults(True,False)
        False

        >>> defaults(False,False)
        True
    """
    result = my_required is my_optional
    return result
