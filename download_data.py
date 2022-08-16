import json
import os

with open('links.json', 'r') as links_json:
    links = json.load(links_json)

for link in links:
    os.system(f"wget -P bases_raw {link}")
