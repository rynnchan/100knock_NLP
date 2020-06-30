import random

s = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
print(s)
slist = s.split(' ')
for i in range(len(slist)):
    if len(slist[i])>4:
        l = slist[i]
        slist[i] = l[0] + ''.join(random.sample(l[1:-1],len(l)-2)) + l[-1]
print(' '.join(slist))