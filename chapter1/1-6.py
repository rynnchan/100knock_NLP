def ngram(n,string):
    l = list()
    for i in range(len(string)-n+1):
        l.append(string[i:i+n])
    return l

X = ngram(2,'paraparaparadise')
Y = ngram(2,'paragraph')

X_dup = set(X) # dup = duplicate 
Y_dup = set(Y) # list(dict.fromkeys(A))

print('和集合',X_dup | Y_dup)
print('積集合',X_dup & Y_dup)
print('差集合',X_dup - Y_dup)

print('\'se\'がXに含まれるか:','se' in X)
print('\'se\'がYに含まれるか:','se' in Y)