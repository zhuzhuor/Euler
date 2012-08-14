#!/usr/bin/env pypy

dict_sets = {}

for i in range(100, 10000):
    cube = i ** 3
    most = int(''.join(sorted(list(str(cube)), reverse=True)))
    if most in dict_sets:
        dict_sets[most]['set'].add(cube)
    else:
        dict_sets[most] = {
                'set': set([cube]),
                'min': cube,
        }

results = [dict_sets[x]['min']
        for x in dict_sets if len(dict_sets[x]['set']) == 5]
print sorted(results)[0]
