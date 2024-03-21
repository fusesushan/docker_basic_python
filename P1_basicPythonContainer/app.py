import pandas as pd
import os

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Paris', 'London', 'Sydney']
}

df = pd.DataFrame(data)

folder_path = 'output'
file_name = 'sample_data.csv'

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f"Folder '{folder_path}' created successfully.")

file_path = os.path.join(folder_path, file_name)

df.to_csv(file_path, index=False)

print("Data has been written to", file_path)
