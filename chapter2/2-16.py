import math
import sys
args = sys.argv
N = int(args[1])
with open('popular-names.txt') as f:
    s = f.read().split('\n')
    length = len([r for r in s if r is not ""])
    num = math.ceil(length/N)
    point = N*num - length
    l = []
    a,b = 0,num
    for i in range(N):
        if i == N-point-1:
            num = num-1
        l.append(s[a:b])
        print(a,b,len(s[a:b]))
        a,b = b,b+num

# split