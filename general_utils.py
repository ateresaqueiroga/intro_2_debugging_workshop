# general_utils.py
#
# This module provides utility functions for exporting and importing DataFrames to and from CSV files.
# 
# INPUTS
# ---------
# df (pandas.DataFrame): The DataFrame to be exported.
# filename (str)       : The path and name of the CSV file to export the DataFrame to.
# 
# OUTPUTS
# ---------
# None for the export function.
# pandas.DataFrame for the import function.
# 
# The module contains functions that handle exporting a DataFrame to a CSV file and importing a CSV file into a DataFrame.
# It demonstrates an example of where a subtle bug in file path handling can occur.
# 
# NOTE: This module was specifically created for the "Introducing Debugging - Unveiling the Power of Code Inspection"
# workshop, to illustrate an example where debugging with breakpoints is useful.
#
# -----------------------------------------------------------------------------------------
# Ana Teresa Queiroga, 2024
# PhD student @ Department of Clinical Medicine, Center for Music in the Brain
# Aarhus University, Denmark


import pandas as pd

def export_to_csv(df, filename):
    """
    Export a DataFrame to a CSV file.

    Parameters:
    df (pandas.DataFrame): The DataFrame to be exported.
    filename (str): The path and name of the CSV file to export the DataFrame to.

    Note:
    This function contains a bug where it incorrectly adds a leading slash to the filename 
    if it doesn't already start with one. This can lead to an invalid file path on most systems.
    
    Example:
    >>> df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
    >>> export_to_csv(df, 'output.csv')
    This will attempt to save the DataFrame to '/output.csv', which may result in an error.
    """
    # Incorrectly handling the file path by adding an extra slash
    if not filename.startswith('/'):
        filename = '/' + filename  # This line is buggy
    df.to_csv(filename, index=False)
    
    

def load_csv_to_dataframe(filename):
    """
    Load a CSV file into a DataFrame.

    Parameters:
    filename (str): The path and name of the CSV file to load.

    Returns:
    pandas.DataFrame: The loaded DataFrame from the specified CSV file.

    Example:
    >>> df = load_csv_to_dataframe('output.csv')
    This will load the DataFrame from 'output.csv' into the variable df.
    """
    return pd.read_csv(filename)
