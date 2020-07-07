import sys
args = sys.argv
N = int(args[1])

with open('popular-names.txt') as f:
    s = f.read()
    for line in s.split('\n')[:N]:
        print(line)

# head -n N popular-names.txt