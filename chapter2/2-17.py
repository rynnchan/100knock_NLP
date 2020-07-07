with open('popular-names.txt') as f:
    s = f.readlines()
    names = set()
    for line in s:
        l = line.split('\t')
        names.add(l[0])
    print(len(names))

# cut
# sort
# uniq