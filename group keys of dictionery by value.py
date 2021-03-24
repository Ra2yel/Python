
d  = {'1': 'Randy', '2': 'Stan', '3': 'Randy', '4': 'Stan', '5': 'Alex', '6': 'Stan'}
new_d = {}
new_d1 = {}

for k in d:
    if d[k] not in new_d.keys():
        new_d[d[k]] = [k]
    else:
        new_d[d[k]].append(k)
print(new_d)


for k,v in d.items():
    if v not in new_d1.keys():
        new_d1[v] = [k]
    else:
        new_d1[v] = new_d1[v] + [k]
print(new_d1