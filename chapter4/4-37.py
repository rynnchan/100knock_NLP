import collections
import matplotlib.pyplot as plt

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
words = []
for l in token_list:
    if '猫' in [morpheme['surface'] for morpheme in l] :
        for morpheme in l:
            if morpheme['surface'] != '猫' and morpheme['pos'] != '記号':
                words.append(morpheme['surface'])
c = collections.Counter(words)
keys, counts = zip(*c.most_common()[:10])
plt.rcParams["font.family"] = "IPAexGothic"
plt.bar(keys, counts,width=0.9)
plt.show()