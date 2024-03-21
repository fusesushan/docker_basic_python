import os
import matplotlib.pyplot as plt

def visualize_data(data, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Create a simple bar chart to visualize data
    plt.bar(data.index, data.values)
    plt.xlabel("Feature")
    plt.ylabel("Value")
    plt.title("Data Visualization")
    image_path = os.path.join(output_dir, "data_visualization.png")
    plt.savefig(image_path)  # Save the plot as an image
    plt.close()  # Close the plot to avoid displaying it

    # Return the path to the saved image
    return image_path
