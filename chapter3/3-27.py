import json
import gzip
import re

with gzip.open('jawiki-country.json.gz', 'r') as f:
    for line in f:
        data = json.loads(line)
        if data['title'] == 'イギリス':
            text = data['text']
            break

pattern = r'^\{\{基礎情報.*^\}\}$'
template = '\n'.join(re.findall(pattern,text,flags=re.MULTILINE|re.DOTALL))
pattern = r'\'{2,5}'
temp_emphansis = re.sub(pattern,'',template)
pattern = r'\[\[(.*?)\]\]'
temp_link = re.sub(pattern,r'\1',temp_emphansis)
pattern = r'^\|(.*?) = (.*?)$'
field = dict(re.findall(pattern,temp_link,flags=re.MULTILINE))
for key,value in field.items():
    print(key+' = '+value)