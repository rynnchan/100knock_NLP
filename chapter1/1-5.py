def ngram(n,string):
    l = list()
    for i in range(len(string)-n+1):
        l.append(string[i:i+n])
    return l

s = 'I am an NLPer'
print(ngram(2,s.split(' ')))
print(ngram(2,s))