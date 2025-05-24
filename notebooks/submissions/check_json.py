# Load a json file

import json

def count_unique_ids(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Extract all IDs and convert to set to get unique values
    unique_ids = set(item['id'] for item in data)
    
    print(f"Total number of unique IDs: {len(unique_ids)}")
    return len(unique_ids)

# Example usage:
count_unique_ids('/Volumes/T7/OMSCS/CLEF2025/EXIST2025/exist-2025/notebooks/submissions/task3_1_soft_DS@GT EXIST_1.json')