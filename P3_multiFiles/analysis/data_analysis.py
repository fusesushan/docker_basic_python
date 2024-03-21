import pandas as pd

def process_data(input_file):
    # Read input data from CSV file
    data = pd.read_csv(input_file)
    
    # Perform some data processing (e.g., calculate mean)
    mean_values = data.mean()
    
    return mean_values
