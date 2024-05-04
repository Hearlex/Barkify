import csv
import json
import os

def generate_json(file):
    name = file.split('.')[0]
    with open(os.path.join("cv-corpus-17.0-2024-03-15-hu/cv-corpus-17.0-2024-03-15/hu", file), 'r', encoding='utf-8') as f:
        data = csv.DictReader(f, delimiter='\t')
        json_data = []
        for row in data:
            json_data.append({
                'name': row['path'].split('_')[-1].split('.')[0],
                'path': row['path'],
                'text': row['sentence'],
                'age': row['age'],
                'gender': row['gender'],
                'accents': row['accents']
            })
            
        with open(f'datasets/{name}.json', 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)

generate_json('train.tsv')
generate_json('test.tsv')