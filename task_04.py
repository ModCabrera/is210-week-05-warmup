#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Function to find enough Catfood and Litter for Cats."""

def too_many_kittens(kittens, litterboxes, catfood=bool()):
    """
    Fuction to find catfood and litterboxes for cats.

    Args:
        kittens (mixed): Arg to catfood to verify truthiness.
        litterboxes (int): Arg to compare greater than or equal to kittens and catfood.
        catfood (bool): Arg to compare truthiness with kittens.

    Returns:
        bool: True if there is more,False if there is not more (litterboxes than kittens and there is catfood.).

    Examples:
        >>> too_many_kittens(12,12,False)
        True
        >>> too_many_kittens(13,12,True)
        True
        >>> too_many_kittens(12,13,True)
        False
    """
    result= not(litterboxes >= kittens and catfood)
    return result
