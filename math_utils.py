# math_utils.py
#
# This module provides utility functions for various mathematical operations on lists.
# 
# INPUTS
# ---------
# data (list): A list of numerical values to be processed by the functions.
# multiplier (int or float): A numerical value by which each element in the list will be multiplied.
# 
# OUTPUTS
# ---------
# A list of processed numerical values or a single numerical value, depending on the function.
# 
# The module contains functions for squaring each element in a list, computing the sum of squares, and multiplying 
# each element by a given multiplier. It includes an example of a subtle bug in the sum of squares function due to an off-by-one error.
# 
# NOTE: This module was specifically created for the "Introducing Debugging - Unveiling the Power of Code Inspection"
# workshop, to illustrate an example where debugging with breakpoints is useful.
#
# -----------------------------------------------------------------------------------------
# Ana Teresa Queiroga, 2024
# PhD student @ Department of Clinical Medicine, Center for Music in the Brain
# Aarhus University, Denmark


def square_elements(data):
    """
    Square each element in the list.

    Parameters:
    data (list): A list of numerical values to be squared.

    Returns:
    list: A list containing the squares of the input values.

    Example:
    >>> square_elements([1, 2, 3])
    [1, 4, 9]
    """
    return [x ** 2 for x in data]



def sum_of_squares(data):
    """
    Return the sum of squares of the list elements.

    Parameters:
    data (list): A list of numerical values.

    Returns:
    int or float: The sum of the squares of the input values.

    Note:
    This function contains a bug where it incorrectly sums all but the last element in the list,
    leading to an off-by-one error. This can result in an incorrect sum of squares.
    
    Example:
    >>> sum_of_squares([1, 2, 3])
    5  # Incorrect output; should be 14
    """
    # Incorrect summation range leading to an off-by-one error
    return sum(data[:-1])  # This line is buggy; it should be sum([x ** 2 for x in data])



def multiply_elements(data, multiplier):
    """
    Multiply each element in the list by the given multiplier.

    Parameters:
    data (list): A list of numerical values to be multiplied.
    multiplier (int or float): The multiplier by which each element in the list will be multiplied.

    Returns:
    list: A list containing the multiplied values.

    Example:
    >>> multiply_elements([1, 2, 3], 2)
    [2, 4, 6]
    """
    return [x * multiplier for x in data]
