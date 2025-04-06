import random
import os
from typing import Dict, List, Any

valid_types = {'int', 'string', 'float', 'date'}

def validate_schema(schema: List[Dict[str, Any]]) -> bool:
    for field in schema:
        if 'name' not in field or 'type' not in field:
            print(f"Missing 'name' or 'type' in field: {field}")
            return False

        if field['type'] not in valid_types:
            print(f"Invalid type '{field['type']}' in field: {field}")
            return False

        if field['type'] in {'int', 'float'}:
            if 'min' not in field or 'max' not in field:
                print(f"Missing 'min' or 'max' for field: {field}")
                return False

            if not isinstance(field['min'], (int, float)) or not isinstance(field['max'], (int, float)):
                print(f"'Min' / 'Max' invalid.")
                return False

        if field['type'] == 'string':
            if 'choices' not in field or not isinstance(field['choices'], list):
                print(
                    f"Missing or invalid 'choices' for string field: {field}")
                return False

        if field['type'] == 'date':
            if 'min' not in field or 'max' not in field or 'format' not in field:
                print(
                    f"Missing 'min', 'max' or 'format' for date field: {field}")
                return False
    return True


def generate_field_freq(fields):
    chosen_fields = list(set([random.choice(fields) for _ in range(0, random.randint(1, len(fields)))]))
    freq = {}
    min_freq = 0.01
    freq_sum = 0.0

    for field in chosen_fields:
        freq[field] = round(random.uniform(min_freq, 1.0), 2)
        min_freq = round(random.uniform(0.01, 1 - min_freq), 2)
        freq_sum += freq[field]
    
    # Ajustăm suma astfel încât să fie cel puțin 1.0
    if freq_sum < 1.0:
        chosen_field = random.choice(chosen_fields)
        diff = 1.0 - freq_sum
        freq[chosen_field] += diff
    
    return freq


def generate_operator_freq(fields, min_eq=0.7):
    chosen_fields = list(set([random.choice(fields) for _ in range(0, random.randint(1, len(fields)))]))
    freq = {}
    
    for field in chosen_fields:
        freq[field] = round(random.uniform(min_eq, 1.0), 2)
    
    return freq

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)