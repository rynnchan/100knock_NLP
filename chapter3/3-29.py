import json
import gzip
import re
import requests

with gzip.open('jawiki-country.json.gz', 'r') as f:
    for line in f:
        data = json.loads(line)
        if data['title'] == 'イギリス':
            text = data['text']
            break

pattern = r'^\{\{基礎情報.*^\}\}$'
template = '\n'.join(re.findall(pattern,text,flags=re.MULTILINE|re.DOTALL))
pattern = r'\'{2,5}'
template = re.sub(pattern,'',template)
pattern = r'\[\[(.*?)\]\]'
template = re.sub(pattern,r'\1',template)
pattern = r'\[.*?\]'
template = re.sub(pattern,'',template)
pattern = r'ファイル:'
template = re.sub(pattern,'',template)
pattern = r':'
template = re.sub(pattern,'',template)
pattern = r'\{\{(.*?)\}\}'
template = re.sub(pattern,r'\1',template)
pattern = r'https.*? '
template = re.sub(pattern,'',template)
pattern = r'^\|(.*?) = (.*?)$'
field = dict(re.findall(pattern,template,flags=re.MULTILINE))

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "iiprop": "url",
    "titles": "File:" + field['国旗画像']
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

for k, v in PAGES.items():
    print(v['imageinfo'][0]['url'])