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
noun_concat = set()
noun = ''
count = 0
for l in token_list:
    for morpheme in l:
        if morpheme['pos'] == '名詞':
            noun += morpheme['surface']
            count += 1
        elif count >= 2:
            noun_concat.add(noun)
            noun = ''
            count = 0
        else :
            noun = ''
            count = 0
print(noun_concat)