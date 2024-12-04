import json
import re

# Define the regular expression pattern to search for the desired text
pattern = r'"patentCaseMetadata":{"applicationNumberText":{.*?},"filingDate":".*?"'
pattern2 = r',"inventionTitle":{.*?}'
pattern3 = r',"applicationTypeCategory":".*?"'
pattern4 = r',"applicationStatusCategory":".*?"'

# Function to read the file line by line and filter out the desired text
def filter_json_lines(filename, num_lines=2):
    with open(filename, 'r', encoding='utf-8') as file:
        filtered_lines = []

        for line in file:
            match = re.search(pattern, line)
            match2 = re.search(pattern2, line)
            match3 = re.search(pattern3, line)
            match4 = re.search(pattern4, line)

            if match:
                # Concatenate the matched lines to form a valid JSON object
                json_object_str = f"{match.group()}{match2.group()}{match3.group()}{match4.group()}" + "}"

                try:
                    # Parse the JSON object and append it to the list of filtered lines
                    filtered_lines.append(json.loads(json_object_str))
                except json.JSONDecodeError:
                    # Handle the case where the JSON object couldn't be parsed
                    continue

                # Break the loop if we have found enough matches
                if len(filtered_lines) >= num_lines:
                    break

        return filtered_lines

# Replace 'your_file.json' with the path to your actual JSON file
result_lines = filter_json_lines('2023.json')

# Function to create a new JSON file and write the filtered results into it
def write_to_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2)

# Replace 'filtered_results.json' with the desired filename for the new JSON file
write_to_json('filtered_results.json', result_lines)
