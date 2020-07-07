import collections

with open('popular-names.txt') as f:
    s = f.readlines()
    names = []
    for line in s:
        l = line.split('\t')
        names.append(l[0])
    values, counts = zip(*collections.Counter(names).most_common())
    for value,count in zip(values,counts):
        print(value,count)

# cut
# sort
# uniq