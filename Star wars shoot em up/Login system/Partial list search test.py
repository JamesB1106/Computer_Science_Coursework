L = ['ones', 'twos', 'thr,ee,s']
wanted = 'th'
items = []
newList = list(filter(lambda x: x.startswith(wanted), L))
for x in newList:
    items.append(x.split(','))
print (items)
