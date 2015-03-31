#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Function to find enough Catfood and Litter for Cats."""



def too_many_kittens(kittens, litterboxes, catfood=bool()):
    """Evaluates if there is enough litterboxes for each kitten, and if catfood.

    Args:
        kittens (int): The number of kittens.
        litterboxes (int): The number of litterboxes.
        catfood (bool): Arg to compare truthiness with kittens.

    Returns:
        result (bool): True if enough litterboxes for kitten and if catfood.

    Examples:
        >>> too_many_kittens(12,12,False)
        True
        >>> too_many_kittens(13,12,True)
        True
        >>> too_many_kittens(12,13,True)
        False
    """
    result = not(litterboxes >= kittens and catfood)
    return result
