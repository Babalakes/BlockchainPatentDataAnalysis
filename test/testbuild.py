import json

# Specify the file path
file_path = "build.json"

# Read the JSON data from the file
with open(file_path, "r") as file:
    data = file.read()

# Convert the data into a list of JSON objects
json_objects = json.loads(data)

# Iterate through each JSON object and print the required information
for obj in json_objects:
    country_code = obj["countryCode"]
    population_2021 = obj["population"]["refYear"]["2021"]["value"]
    internet_users_2022 = obj["internetUsers"]["refYear"]["2022"]["value"]

    print(f"Country Code: {country_code}")
    print(f"Population in 2021: {population_2021}")
    print(f"Internet Users in 2022: {internet_users_2022}")
    print()
