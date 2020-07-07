import sys
args = sys.argv
N = int(args[1])

with open('popular-names.txt') as f:
    s = f.read()
    for line in s.split('\n')[-N-1:-1]:
        print(line)

# tail -n N popular-names.txt