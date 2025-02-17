import json

import re


# Define the regular expression pattern to search for the desired text

pattern = r'"patentCaseMetadata":{"applicationNumberText":{.*?}'

pattern2 = r',"inventionTitle":{.*?}'

# Function to read the file line by line and filter out the desired text

def filter_json_lines(filename, num_lines=5):

    with open(filename, 'r', encoding='utf-8') as file:

        filtered_lines = []

        filtered_lines2 = []

        for line in file:

            match = re.search(pattern, line)

            match2 = re.search(pattern2, line)


            if match and match2:

                # Append the line to the list of filtered lines

                filtered_lines.append(match.group())

                filtered_lines2.append(match2.group())


            # Break the loop if we have found enough matches

            if len(filtered_lines and filtered_lines2) >= num_lines:

                break


    return filtered_lines, filtered_lines2


# Replace 'your_file.json' with the path to your actual JSON file


result_lines = filter_json_lines('2023.json')


# Print the first 5 lines of the filtered result

if result_lines:

    for line in result_lines:

        print(line)

else:

    print("No matches found for the specified pattern in the JSON file.")