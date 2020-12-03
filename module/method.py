

def search(a):
    total = readfi()
    memo = []
    me = []
    ser = a['entry1']
    for i in range(len(total)):
        if ser in total[i][int(a['ent'])]:
            memo.append(i)
    if len(memo)==0:
        return ['ヒットなし']
    for i in range(len(memo)):
        me.append(total[memo[i]][0]+"系"+total[memo[i]][1]+"： "+total[memo[i]][2])
    return me

def readfi():
    path = 'data/dataset.txt'
    typ = []
    syu = []
    man = []
    total = []
    with open(path) as f:
        for s_line in f:
            me = []
            me.append(s_line.split()[0])
            me.append(s_line.split()[1])
            me.append(s_line.split()[2])
            total.append(me)
    return total