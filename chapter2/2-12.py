with open('popular-names.txt') as f:
    s = f.readlines()

with open('col1.txt',mode='w') as f1, open('col2.txt',mode='w') as f2:
    for line in s:
        l = line.split('\t')
        f1.write(l[0]+'\n')
        f2.write(l[1]+'\n')

# cat popular-names.txt | cut -f 1
# cat popular-names.txt | cut -f 2