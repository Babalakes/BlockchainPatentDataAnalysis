import json
import pandas as pd

# Specify the file path
file_path = "build.json"

# Read the JSON data from the file
with open(file_path, "r") as file:
    data = json.load(file)

# Convert the JSON data into a DataFrame
df = pd.DataFrame(data)

# Specify the output Excel file path
output_file_path = "countries_data.xlsx"

# Save the DataFrame to an Excel workbook
df.to_excel(output_file_path, index=False)

print(f"Data has been successfully converted and saved to {output_file_path}.")
