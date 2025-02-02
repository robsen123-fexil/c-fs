cnt=0
a , b = (map (int, input().split()))
lists=list(map(int , input().split()))
value=lists[b-1]
for i in lists:
    if i>=value:
        cnt+=1
print(cnt)