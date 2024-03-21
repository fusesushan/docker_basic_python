import os
from analysis.data_analysis import process_data
from analysis.visualization import visualize_data

def main():
    input_file = "data/inputdata.csv"
    processed_data = process_data(input_file)
    print("Processed data:", processed_data)
    
    # Specify the output directory
    output_dir = "output"
    visualization_path = visualize_data(processed_data, output_dir)
    print("Data visualization saved as:", visualization_path)

if __name__ == "__main__":
    main()
