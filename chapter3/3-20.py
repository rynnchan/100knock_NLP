import json
import gzip

with gzip.open('jawiki-country.json.gz', 'r') as f:
    for line in f:
        data = json.loads(line)
        if data['title'] == 'イギリス':
            text = data['text']
            break
print(text)