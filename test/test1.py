import pandas as pd
import json

def print_first_two_lines(json_file_path):
    with open(json_file_path, 'r') as json_file:
        line_count = 0
        for line in json_file:
            print('YOURS', line)
            line_count += 1
            if line_count >= 2:
                break

if __name__ == "__main__":
    json_file_path = "2000.json"
    print_first_two_lines(json_file_path)

