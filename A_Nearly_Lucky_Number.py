from collections import Counter
n=int(input())
strs=str(n)
cnt=Counter(strs)
count=0
for k , v in cnt.items():
    if k=='4' or k=='7':
        count+=v
if count==4 or count==7:
    print('YES')
else:
    print('NO')