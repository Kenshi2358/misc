"""
This script converts a json file (containing a single level of nested JSON) to a csv using Pandas.

A json is a file containing a key-value pairs like a python dictionary.

Note: a flattened json is one where the value for every field is one value.
There is no nested json structure. All fields are first-level properties.

A nested json structure is one where the value can be another dictionary of key-value pairs.

To convert an N-level nested JSON to csv, you'll need to use the json_normalize() method in Pandas.
"""

import json
import pandas

def read_json(filename: str) -> dict: 

    try: 
        with open(filename, "r") as f: 
            data = json.loads(f.read()) 
    except: 
        raise Exception(f"Reading {filename} file encountered an error") 

    return data 


def normalize_json(data: dict) -> dict: 

    new_data = dict() 
    for key1, value1 in data.items(): 
        if not isinstance(value1, dict): 
            new_data[key1] = value1 
        else: 
            for key2, value2 in value1.items():
                new_key_str = f"{key1}_{key2}"
                new_data[new_key_str] = value2 

    return new_data 


def main(): 

    input_file1 = "json_conversion_test1.json"

    # Read the JSON file as python dictionary 
    data = read_json(filename=input_file1) 

    # Normalize the nested python dict  
    new_data = normalize_json(data=data) 

    print("New dict:", new_data, "\n") 

    # Create a pandas dataframe  
    dataframe = pandas.DataFrame(new_data, index=[0]) 

    # Write to a CSV file 
    dataframe.to_csv("json_converted.csv") 


if __name__ == '__main__': 
    main() 