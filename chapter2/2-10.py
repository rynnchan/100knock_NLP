with open('popular-names.txt') as f:
    s = f.read()
    print(len([r for r in s.split('\n') if r is not ""]))

# cat popular-names.txt | wc -l