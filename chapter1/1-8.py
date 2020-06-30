def cipher(s):
    return ''.join([chr(219-ord(i)) if i.islower() else i for i in s])

s = 'aAbBcCxXyYzZ'
s_cip = cipher(s)
print(s_cip)
s_decip = cipher(s_cip)
print(s_decip)