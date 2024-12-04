import json
import re

# Define the regular expression pattern to search for the desired text
pattern = r'"patentCaseMetadata":{"applicationNumberText":{.*?}'
# Function to read the file line by line and filter out the desired text
def filter_json_lines(filename, num_lines=5):
    with open(filename, 'r', encoding='utf-8') as file:
        filtered_lines = []
        for line in file:
            match = re.search(pattern, line)
            if match:
                filtered_lines.append(match.group())

            # Break the loop if we have found enough matches
            if len(filtered_lines) >= num_lines:
                break

    return filtered_lines

# Replace 'your_file.json' with the path to your actual JSON file
result_lines = filter_json_lines('2023.json')

# Print the first 5 lines of the filtered result
if result_lines:
    for line in result_lines:
        print(line)
else:
    print("No matches found for the specified pattern in the JSON file.")
