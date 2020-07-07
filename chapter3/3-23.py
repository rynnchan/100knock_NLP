import json
import gzip
import re

with gzip.open('jawiki-country.json.gz', 'r') as f:
    for line in f:
        data = json.loads(line)
        if data['title'] == 'イギリス':
            text = data['text']
            break

pattern = r'(\={2,})\s*(.*?)\={2,}'
print('\n'.join(i[1]+':'+str(len(i[0])-1) for i in re.findall(pattern,text)))