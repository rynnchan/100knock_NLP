with open('col1.txt') as f1, open('col2.txt') as f2:
    #s1 = [s.strip() for s in f1.readlines()]
    s1 = f1.read().splitlines()
    s2 = f2.readlines()

with open('merge.txt',mode='w') as m:
    for line1,line2 in zip(s1,s2):
        m.write(line1+'\t'+line2)

# paste col[1-2].txt