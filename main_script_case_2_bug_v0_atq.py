# main_script_case_2_bug_v0_atq.py
#
# This script demonstrates the use of utility functions for mathematical operations and file handling.
#
# INPUTS
# ---------
# data (list): A list of numerical values to be processed.
#
# OUTPUTS
# ---------
# None
#
# The script performs the following operations:
# 1. Squares each element in the provided list.
# 2. Computes the sum of the squared elements.
# 3. Creates a DataFrame containing the original and squared values.
# 4. Exports the DataFrame to a CSV file.
# 5. Prints the original data, squared data, sum of squares, and the path to the exported CSV.
#
# NOTE: This script was specifically created for the "Introducing Debugging - Unveiling the Power of Code Inspection"
# workshop, to illustrate an example where debugging with breakpoints is useful.
#
#intro_2_debugging_workshop/
#├── main_script.py
#├── math_utils.py
#├── general_utils.py
#└── output/
#    └── output.csv
#
# -----------------------------------------------------------------------------------------
# Ana Teresa Queiroga, 2024
# PhD student @ Department of Clinical Medicine, Center for Music in the Brain
# Aarhus University, Denmark

import pandas as pd
import math_utils
import general_utils

# Example data
data = [1, 2, 3, 4, 5]

# Perform calculations
squared_data   = math_utils.square_elements(data)
sum_of_squares = math_utils.sum_of_squares(squared_data)

# Create a DataFrame
df = pd.DataFrame({'original': data, 'squared': squared_data})

# Save DataFrame to CSV
export_path = 'output.csv'
general_utils.export_to_csv(df, export_path)

# Print results
print(f"Original data: {data}")
print(f"Squared data: {squared_data}")
print(f"Sum of squares: {sum_of_squares}")
print(f"Data exported to {export_path}")
