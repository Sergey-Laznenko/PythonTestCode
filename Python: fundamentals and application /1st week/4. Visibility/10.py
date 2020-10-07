def get(ns, var):
    if var in space[ns][1]:
        return ns
    elif ns == 'global':
        return 'None'
    return get(space[ns][0], var)


space = {'global': ['None', []]}
for _ in range(int(input())):
    com, ns, param = input().split()
    if com == 'create':
        space[ns] = [param, []]
    elif com == 'add':
        space[ns][1].append(param)
    elif com == 'get':
        print(get(ns, param))
