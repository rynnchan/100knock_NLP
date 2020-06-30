s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
l = s.replace('.','').split(' ')
num = [1,5,6,7,8,9,15,16,19]
result = dict()
for i in range(len(l)):
    if i+1 in num :
        result[l[i][:1]]=i+1
    else :
        result[l[i][:2]]=i+1
print(result)