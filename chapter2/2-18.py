with open('popular-names.txt') as f:
    s = f.read().splitlines()
    for i in range(len(s)):
        s[i] = s[i].split('\t')
    s_sort = sorted(s,key=lambda x: x[2],reverse=True)
    for i in s_sort:
        print("\t".join(i))

# sort