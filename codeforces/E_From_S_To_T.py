from collections import Counter
def checker(s, t):
    ss = ''
    cnts = Counter(s)
    cntt = Counter(t)
    for i in s:
        if i in cntt and cntt[i] > 0:
            cntt[i] -= 1
            ss += i
    tt = ''
    pp = ''
    for i in t:
        if i in cnts and cnts[i] > 0:
            cnts[i] -= 1
            tt += i
        else:
            pp += i
    if ss == tt:
        return ['YES', pp]
    else:
        return ['NO']
q = int(input())
for _ in range(q):
    s = input().strip()
    t = input().strip()
    p = input().strip()
    result = checker(s, t)
    if result[0] == 'YES':
        b = result[1]
        cntp = Counter(p)
        bb = Counter(b)
        for k, v in bb.items():
            if k not in cntp or v > cntp[k]:
                print('NO')
                break
        else:
            print('YES')
    else:
        print('NO')