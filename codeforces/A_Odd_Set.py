t=int(input())
from collections import defaultdict
for _ in range(t):
    n=int(input())
    lists=list(map (int , input().split()))
    cnt=defaultdict(list)
    cnt[0].append(0)
    cnt[1].append(0)
    for i in range(len(lists)):
        cnt[lists[i]%2].append(lists[i])
    cnts=dict(sorted(cnt.items() , key=lambda x:x[1]))
    mx=max(cnt.values())
    
    mx=0
    for v in cnt.values():
        mx=max(mx , len(v))
    flag=True;
    for v in cnts.values():
        if mx!=(len(v)):
            print('No')
            flag=False
            continue
    if flag:

        print('Yes' )