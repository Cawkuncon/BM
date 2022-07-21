a = {}

for i in list('abc'):
    a[i] = {}
    for j in range(3):
        a[i]['sadasd'] = None
print(a)

b = a['a'].get('sadasd', 1)
print(b)


