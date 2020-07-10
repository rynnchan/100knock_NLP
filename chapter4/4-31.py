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
surface = set()
for l in token_list:
    for morpheme in l:
        if morpheme['pos'] == '動詞':
            surface.add(morpheme['surface'])
print(surface)