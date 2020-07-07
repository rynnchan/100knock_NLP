import json
import gzip
import re

with gzip.open('jawiki-country.json.gz', 'r') as f:
    for line in f:
        data = json.loads(line)
        if data['title'] == 'イギリス':
            text = data['text']
            break

pattern = r'\[\[Category:(.*?)(?:\|\*)?\]\]'
print('\n'.join(re.findall(pattern,text)))