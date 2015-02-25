#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Creating a Function"""


def defaults(my_required, my_optional=True):
    """False Testing function.

    Args:
        my_required (mixed): Args is compared if same as my_optional.
        my_optional (bool): Args is compared if same as my_required.

    Returns:
        bool: All arguments tested for validity.
        
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
