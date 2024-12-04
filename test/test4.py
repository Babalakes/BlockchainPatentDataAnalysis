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
        filtered_lines2 = []
        filtered_lines3 = []
        filtered_lines4 = []

        for line in file:
            match = re.search(pattern, line)
            match2 = re.search(pattern2, line)
            match3 = re.search(pattern3, line)
            match4 = re.search(pattern4, line)

            if match and match2 and match3 and match4:
                # Append the line to the list of filtered lines
                filtered_lines.append(match.group())
                filtered_lines2.append(match2.group())
                filtered_lines3.append(match3.group())
                filtered_lines4.append(match4.group())

                # Break the loop if we have found enough matches
                if len(filtered_lines) >= num_lines:
                    break

        return list(zip(filtered_lines, filtered_lines2, filtered_lines3, filtered_lines4))

# Replace 'your_file.json' with the path to your actual JSON file
result_lines = filter_json_lines('2023.json')

# Print the first 5 lines of the filtered result
if result_lines:
    for line1, line2, line3, line4 in result_lines:
        print(f"{line1}{line2}{line3}{line4}","}","\n", end="")
else:
    print("No matches found for the specified pattern in the JSON file.")
