import pandas as pd
import math_utils
import general_utils

def main():
    # Example data
    data = [1, 2, 3, 4, 5]
    
    # Perform calculations
    squared_data = math_utils.square_elements(data)
    sum_of_squares = math_utils.sum_of_squares(squared_data)
    
    # Create a DataFrame
    df = pd.DataFrame({'original': data, 'squared': squared_data})
    
    # Save DataFrame to CSV
    general_utils.export_to_csv(df, 'output.csv')
    
    # Print results
    print(f"Original data: {data}")
    print(f"Squared data: {squared_data}")
    print(f"Sum of squares: {sum_of_squares}")

if __name__ == "__main__":
    main()
