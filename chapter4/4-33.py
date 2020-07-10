with open('neko.txt.mecab') as f:
    s = f.read().splitlines()
    token_list = []
    token = []
    for morpheme in s:
        if morpheme == 'EOS':
            if token != []:
                token_list.append(token)
                token = []
            continue
        elif morpheme == '':
            continue
        morpheme_sp = morpheme.split(',')
        sur_spe = morpheme_sp[0].split('\t')
        if sur_spe[0] == '':
            continue
        token.append(
            dict(
                surface = sur_spe[0],
                base = morpheme_sp[6],
                pos = sur_spe[1],
                pos1 = morpheme_sp[1]
            )
        )
noun = set()
for l in token_list:
    for i in range(1,len(l)-1):
        if l[i-1]['pos'] == '名詞' and l[i]['surface'] == 'の' and l[i+1]['pos'] == '名詞':
            noun.add(l[i-1]['surface']+l[i]['surface']+l[i+1]['surface'])
print(noun)