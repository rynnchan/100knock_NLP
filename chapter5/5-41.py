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
        morpheme_sp = morpheme.split(',')
        sur_spe = morpheme_sp[0].split('\t')
        morphs.append(Morph(sur_spe[0],morpheme_sp[6],sur_spe[1],morpheme_sp[1]))

for chunk in token_list[1]:
    print([morph.surface for morph in chunk.morphs], chunk.dst, chunk.srcs)