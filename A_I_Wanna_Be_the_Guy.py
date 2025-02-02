level=int(input())
p=list(map (int , input().split()))
q=list(map(int , input().split()))
pq=p[1:]+q[1:]
from collections import Counter
cnt=Counter(pq)
if len(cnt)>=level:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')