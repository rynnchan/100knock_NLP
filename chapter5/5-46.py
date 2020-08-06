from collections import OrderedDict

class Morph:
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

class Chunk:
    def __init__(self,morphs,dst):
        self.morphs = morphs
        self.dst = dst
        self.srcs = []

with open('ai.ja.txt.parsed') as f:
    s = f.read().splitlines()
    token_list = []
    chunks = []
    morphs = []
    for morpheme in s:
        if morpheme[0] == '*':
            if morphs != []:
                chunks.append(Chunk(morphs,dst))
                morphs = []
            dst = int(morpheme.split(' ')[2].rstrip('D'))
            continue
        elif morpheme == 'EOS':
            if morphs != []:
                chunks.append(Chunk(morphs,dst))
                for i in range(len(chunks)):
                    if chunks[i].dst != -1:
                        chunks[chunks[i].dst].srcs.append(i)
                token_list.append(chunks)
                morphs = []
                chunks = []
            continue
        else :
            morpheme_sp = morpheme.split(',')
            sur_spe = morpheme_sp[0].split('\t')
            morphs.append(Morph(sur_spe[0],morpheme_sp[6],sur_spe[1],morpheme_sp[1]))

    #token = token_list[1]
for token in token_list:
    for i in range(len(token)):
        if token[i].srcs != []:
            for morph in token[i].morphs:
                if morph.pos == '動詞':
                    base = morph.base
                    terms = {}
                    for j in token[i].srcs:
                        for morph_srcs in token[j].morphs:
                            if morph_srcs.pos == '助詞':
                                terms[morph_srcs.surface] = ''.join([morph.surface for morph in token[j].morphs if morph.pos != '記号'])
                    if terms != {}:
                        terms = OrderedDict(sorted(terms.items(), key=lambda x:x[0]))
                        keys,values = terms.keys(),list(dict.fromkeys(terms.values()))
                        print('{}\t{}\t{}'.format(base,' '.join(keys),' '.join(values)))
                    break