

def search(a):
    typ, syu, man = readfi()
    memo = []
    me = []
    for i in range(len(man)):
        if a in man[i]:
            memo.append(i)
    if len(memo)==0:
        return ['ヒットなし']
    for i in range(len(memo)):
        me.append(typ[memo[i]]+"系"+syu[memo[i]]+"： "+man[memo[i]])
    return me


def readfi():
    path = 'data/dataset.txt'
    typ = []
    syu = []
    man = []
    with open(path) as f:
        for s_line in f:
            typ.append(s_line.split()[0])
            syu.append(s_line.split()[1])
            man.append(s_line.split()[2])
    return typ,syu,man