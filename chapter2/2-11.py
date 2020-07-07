with open('popular-names.txt') as f:
    s = f.read()
    print(s.replace('\t',' '))

# cat popular-names.txt | sed s/$'\t'/" "/g     sed "s/\t/\ /g" は駄目だった(Mac)
# cat popular-names.txt | tr "\t" " "
# expand -t 1 popular-names.txt