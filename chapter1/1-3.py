s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
l = s.replace(',','').replace('.','').split(' ')
result = [len(i) for i in l]
print(result)