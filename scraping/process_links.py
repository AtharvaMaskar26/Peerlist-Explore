import json 
from utils import convert_link

project_data = []

with open("unprocessed_links.json", 'r') as json_file: 
    project_data = json.load(json_file)

for project in project_data:
    project['project_link'] = convert_link(project['project_link'])

with open("processed_links.json", 'w') as json_file:
    json.dump(project_data, json_file, indent=4)